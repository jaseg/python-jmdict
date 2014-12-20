#!/usr/bin/env python3

import lzma
import pickle
from enum import Enum
from collections import namedtuple

class EntryType(Enum):
	surname		= 1
	place  		= 2
	unclass		= 3
	company		= 4
	product		= 5
	work   		= 6
	masc   		= 7
	fem	   		= 8
	person 		= 9
	given  		= 10
	station		= 11
	organization= 12
	oik			= 13

	ENTRY_TYPES = {
			"family or surname":							surname,
			"place name":									place,
			"unclassified name":							unclass,
			"company name":									company,
			"product name":									product,
			"work of art, literature, music, etc. name":	work,
			"male given name or forename":					masc,
			"female given name or forename":				fem,
			"full name of a particular person":				person,
			"given name or forename, gender not specified":	given,
			"railway station":								station,
			"organization name":							organization,
			"old or irregular kana form" :					oik }
	ENTRY_DESCRIPTIONS = { v:k for k,v in ENTRY_TYPES.items() }

	def __str__(self):
		return ENTRY_DESCRIPTIONS[self]

Translation	= namedtuple('Translation', ['translations', 'types'])
Entry		= namedtuple('Entry', ['kanji', 'readings', 'translations'])

if __name__ == '__main__':
	from xml.etree.ElementTree import ElementTree
	from types import SimpleNamespace
	import names

	def _load_jmnedict(fname):
		with lzma.open(fname, 'rt', encoding='utf-8') as f:
			tree = ElementTree()
			tree.parse(f)
	
		data = set()
		def parse_entry(entry):
			kanji = frozenset({ keb.text for ele in entry.findall('k_ele') for keb in ele.findall('keb') })
			readings = frozenset({ reb.text for ele in entry.findall('r_ele') for reb in ele.findall('reb') })
			trans = entry.findall('trans')
			# strip leading & and trailing ; from entity (e.g. "&person;"→"person")
			translations = frozenset({
					names.Translation(tuple( det.text for det in tr.findall('trans_det') ),
								tuple( ENTRY_TYPES[nt.text] for nt in tr.findall('name_type') ))
					for tr in trans })
			return names.Entry(kanji, readings, translations)
		entries = { parse_entry(entry) for entry in tree.getroot().findall('entry') }
		mapping = { key: entry for entry in entries for key in entry.kanji|entry.readings }
		return entries,mapping
	
	entries,mapping = _load_jmnedict('JMnedict.xml.lzma')
	
	with lzma.open('name_data.pickle.lzma', 'wb') as f:
		pickle.dump((entries,mapping), f)
else:
	with lzma.open('name_data.pickle.lzma', 'rb') as f:
		entries,mapping = pickle.load(f)

