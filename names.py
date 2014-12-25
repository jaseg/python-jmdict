#!/usr/bin/env python3

import lzma
import pickle
from enum import Enum
from collections import namedtuple, defaultdict
from operator import itemgetter
from model import *

def nametypes(name):
    d = defaultdict(lambda: 0)
    for e in mapping[name]:
        for t in e.translations:
            for x in t.types:
                d[x] += 1
    return list(reversed(sorted(d.items(), key=itemgetter(1))))

def morae_histogram(indices=slice(None)):
    d = defaultdict(lambda: defaultdict(lambda: 0))
    for e in entries:
        for r in e.readings:
            keys = morae_split(r)[indices]
            for key in keys:
                for t in e.translations:
                    for x in t.types:
                        d[x][key] += 1
                d['total'][key] += 1
    return {k: list(reversed(sorted(vs.items(), key=itemgetter(1)))) for k,vs in d.items()}

if __name__ == '__main__':
    from xml.etree.ElementTree import ElementTree
    from types import SimpleNamespace

    def _load_jmnedict(fname):
        with lzma.open(fname, 'rt', encoding='utf-8') as f:
            tree = ElementTree()
            tree.parse(f)
    
        data = set()
        def parse_entry(entry):
            kanji = [ keb.text for ele in entry.findall('k_ele') for keb in ele.findall('keb') ]
            readings = [ reb.text for ele in entry.findall('r_ele') for reb in ele.findall('reb') ]
            trans = entry.findall('trans')
            # strip leading & and trailing ; from entity (e.g. "&person;"→"person")
            translations = [ NameTranslation([ det.text for det in tr.findall('trans_det') ],
                            [ EntryType(nt.text) for nt in tr.findall('name_type') ])
                    for tr in trans ]
            return Entry(kanji, readings, translations, None)
        entries = [ parse_entry(entry) for entry in tree.getroot().findall('entry') ]
        mapping = groupdict((key, entry) for entry in entries for key in entry.kanji+entry.readings)
        return entries,mapping
    
    entries,mapping = _load_jmnedict('JMnedict.xml.lzma')
    
    with lzma.open('name_data.pickle.lzma', 'wb') as f:
        pickle.dump((entries,mapping), f)
else:
    with lzma.open('name_data.pickle.lzma', 'rb') as f:
        entries,mapping = pickle.load(f)

