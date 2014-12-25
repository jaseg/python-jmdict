#!/usr/bin/env python3

import lzma
import pickle
from model import *

#XXX FIXME convert certaing usages of tuples to sets

if __name__ == '__main__':
    from xml.etree.ElementTree import ElementTree
    from itertools import groupby
    from operator import itemgetter
    import string

    def _load_kradfile(fname):
        with lzma.open(fname, 'rt', encoding='euc-jp') as f:
            splitlines = (line.partition(' : ') for line in f.readlines() if not line.startswith('#'))
            return { kanji: parts.rstrip().split(' ') for kanji,_sep,parts in splitlines }

    def _load_kanjivg(fname):
        with lzma.open(fname, 'rt', encoding='utf-8') as f:
            tree = ElementTree()
            tree.parse(f)
        
        def parse_kanji(kanji):

            # Converts str('kvg:04e17-g7') to int(7) and str('kvg:04e7e-s11') to int(11)
            indexnum    = lambda s: int(s.rpartition('-')[2][1:])
            ididx       = lambda elem: indexnum(elem.attrib['id'])

            strokes = [ stroke.attrib['d'] for stroke in sorted(kanji.findall('.//path'), key=ididx) ]

            gdata = sorted( (((group.attrib.get('element', group.attrib['id']), int(group.attrib.get('number', '0'))), group)
                        for group in kanji.findall('.//g')),
                    key=itemgetter(0))
            # We use 0-indexed stroke numbers here so you can directly use them as indices to the strokes element.
            groups = [ [ ididx(path)-1
                        for (_elem, __number), group in foo
                        for path in group.findall('.//path') ]
                    for (elem, _number), foo in groupby(gdata, itemgetter(0)) ]

            return KanjiVGEntry(strokes, groups)
        
        # Converts str('kvg:kanji_05726') to str('圦')
        kvgchr      = lambda s: chr(int(s[len('kvg:kanji_'):].rstrip(string.ascii_letters+string.punctuation), 16))
        return { kvgchr(kanji.attrib['id']): parse_kanji(kanji) for kanji in tree.findall('kanji') }

    # yes, the two default values *are* ok.
    def _load_kanjidic2(fname, radical_decomposition={}, kanjivg={}):
        with lzma.open(fname, 'rt', encoding='utf-8') as f:
            tree = ElementTree()
            tree.parse(f)

        def decchar(char):
            literal = char.find('literal').text

            cps     = char.find('codepoint')
            rads    = char.find('radical')
            misc    = char.find('misc')
            dns     = char.find('dic_number')       # optional
            qcodes  = char.find('query_code')       # optional
            rms     = char.find('reading_meaning')  # optional

            codepoint   = { cp.attrib['cp_type']: cp.text for cp in cps.findall('cp_value') }

            radicals        = { rad.attrib['rad_type']: rad.text for rad in rads.findall('rad_value') }
            # Nelson data is only present in the file if it differs from the classical classification
            radicals['nelson_c'] = radicals.get('nelson_c', radicals['classical'])

            gr = misc.find('grade')
            grade       = int(gr.text) if gr else None
            
            # Contains the stroke count as a first element, and possibly common miscounts as further elements
            stroke_count    = [ int(sc.text) for sc in misc.findall('stroke_count') ]

            variants        = { var.attrib['var_type']: var.text for var in misc.findall('variant') }

            # Frequency-of-use rank from 1-2501, or None if the kanji is not one of the top 2500.
            freq = misc.find('freq')
            frequency   = int(freq.text) if freq else None

            # radical names in hiragana, if any.
            rad_names   = [ rn.text for rn in misc.find('rad_name') or [] ]

            # old JLPT level from 1 (most advanced) through 4 (most elementary). For the new JLPT with levels from N1 to N5
            # there are no public kanji lists.
            jlpt = misc.find('jlpt')
            jlpt_level  = int(jlpt) if jlpt else None

            dic_numbers = { dn.attrib['dr_type']: dn.text for dn in dns.findall('dic_ref') } if dns else {}
            # If there is a Daikanwajiten index given, include the additional page and volume data as moro_page and moro_vol
            # elements.
            if 'moro' in dic_numbers:
                elem = dns.find("./dic_ref[@dr_type='moro']")
                dic_numbers['moro_vol'] = elem.attrib.get('m_vol')
                dic_numbers['moro_page'] = elem.attrib.get('m_page')
            # Convert dictionary indices to integers where they are certain to be numbers
            NOT_NUMERIC = ('moro', 'busy_people', 'oneill_names')
            bar = lambda v, *vs: map(int, (v,)+vs) if vs is not () else int(v)
            dic_numbers = { k: bar(*v.split()) if v and k not in NOT_NUMERIC else v for k,v in dic_numbers.items() }

            query_codes = { qc.attrib['qc_type']: qc.text for qc in qcodes.findall('q_code')
                    if not 'skip_misclass' in qc.attrib} if qcodes else {}
            # If a skip code is given, include a (possibly empty) list of (misclassification_type, misclassified_skip_code)
            # tuples.
            if 'skip' in query_codes:
                query_codes['skip_misclass'] = tuple( (mc.attrib['skip_misclass'], mc.text)
                        for mc in qcodes.findall('./q_code[@skip_misclass]'))

            def rm_decode(rmg):
                reading_dict = groupdict((el.attrib['r_type'], el.text) for el in rmg.findall('reading'))
                meaning_dict = groupdict((el.attrib.get('m_lang', 'en'), el.text) for el in rmg.findall('meaning'))
                return reading_dict, meaning_dict
            # Tuple of (readings, meanings) tuples where readings is a dict mapping reading types to readings and meanings
            # is a dict mapping language codes to meanings.
            rms_list    = [ rm_decode(rmg) for rmg in rms.findall('rmgroup')] if rms else []
            # Tuple of readings only used in names
            nanori      = [ elem.text for elem in rms.findall('nanori') ] if rms else []

            # link radical decomposition and kanjivg stroke/group data into main entry
            decomposition = radical_decomposition.get(literal)
            kanjivg_entry = kanjivg.get(literal)

            return literal, KanjidicEntry(literal,
                    codepoint,
                    radicals,
                    grade,
                    stroke_count,
                    variants,
                    frequency,
                    rad_names,
                    jlpt_level,
                    dic_numbers,
                    query_codes,
                    rms_list,
                    nanori,
                    decomposition,
                    kanjivg_entry)

        chars = tree.getroot().findall('character')
        return dict( decchar(char) for char in chars )

    radical_decomposition = {}
    radical_decomposition.update(_load_kradfile('kradfile2.lzma'))
    radical_decomposition.update(_load_kradfile('kradfile.lzma'))

    kanjivg = _load_kanjivg('kanjivg.xml.lzma')

    data = _load_kanjidic2('kanjidic2.xml.lzma', radical_decomposition, kanjivg)

    with lzma.open('kanji_data.pickle.lzma', 'wb') as f:
        pickle.dump((radical_decomposition, kanjivg, data), f)

else:
    with lzma.open('kanji_data.pickle.lzma', 'rb') as f:
        radical_decomposition, kanjivg, data = pickle.load(f)
