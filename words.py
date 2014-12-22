#!/usr/bin/env python3

import lzma
import pickle
import itertools
import operator

LANG_ATTR = '{http://www.w3.org/XML/1998/namespace}lang'

    
if __name__ == '__main__':
    from xml.etree.ElementTree import ElementTree
    from types import SimpleNamespace
    from model import *

    groupdict = lambda tupgen: {k: [v for _k,v in vs] for k,vs in itertools.groupby(sorted(tupgen), key=operator.itemgetter(0))}

    def _load_jmdict(fname):
        with lzma.open(fname, 'rt', encoding='utf-8') as f:
            tree = ElementTree()
            tree.parse(f)
    
        data = set()
        def parse_entry(entry):
            kanji       = [Variant(ele.find('keb').text,
                                    [EntryType(inf.text) for inf in ele.findall('ke_inf')],
                                    [pri.text for pri in ele.findall('ke_pri')])
                                for ele in entry.findall('k_ele')]
            # FIXME ignoring re_restr for now
            readings    = [Variant(ele.find('reb').text,
                                    [EntryType(inf.text) for inf in ele.findall('re_inf')] +
                                    ([EntryType('nokanji')] if ele.find('re_nokanji') else []),
                                    [pri.text for pri in ele.findall('re_pri')])
                                for ele in entry.findall('r_ele')]
            # NOTE: We are ignoring any <etym>, <bibl> or <audit> elements. The former two are not in use as of the time
            # this code is written (September 2014) and the latter one does not seem interesting at the moment. - jaseg
            links       = [Link(link.find('link_tag').text,
                                         link.find('link_desc').text,
                                         link.find('link_uri').text)
                                     for info in entry.findall('info')
                                     for link in info.findall('links')]

            # NOTE: For now, we are ignoring the g_gend attribute as well as the <pri> and <example> elements since
            # these are not used at the time this code is written (September 2014). - jaseg
            # <!ELEMENT sense (s_inf*, lsource*, gloss*)>
            sense_elems     = entry.findall('sense')
            translations = []
            for sense in sense_elems:
                stagk       = [stagk.text for stagk in sense.findall('stagk')]
                stagr       = [stagr.text for stagr in sense.findall('stagr')]
                pos         = [EntryType(pos.text) for pos in sense.findall('pos')]
                xref        = [xref.text for xref in sense.findall('xref')]
                ant         = [ant.text for ant in sense.findall('ant')]
                field       = [field.text for field in sense.findall('field')]
                misc        = [EntryType(misc.text) for misc in sense.findall('misc')]
                dial        = [EntryType(dial.text) for dial in sense.findall('dial')]
                sinf        = [inf.text for inf in sense.findall('s_inf')]
                gloss_dict  = groupdict((gloss.get(LANG_ATTR, 'eng'), gloss.text) for gloss in sense.findall('gloss'))
                gloss       = gloss_dict['eng']
                translations.append(Translation(gloss, gloss_dict, stagk, stagr, pos, xref, ant, field, misc, dial, sinf))

            return Entry(kanji, readings, translations, links)
        entries = [ parse_entry(entry) for entry in tree.getroot().findall('entry') ]
        mapping = groupdict((key.moji, entry) for entry in entries for key in entry.kanji+entry.readings)
        return entries,mapping
    
    entries,mapping = _load_jmdict('JMdict.xml.lzma')
    
    with lzma.open('word_data.pickle.lzma', 'wb') as f:
        pickle.dump((entries,mapping), f)
else:
    from model import *
    with lzma.open('word_data.pickle.lzma', 'rb') as f:
        entries,mapping = pickle.load(f)

