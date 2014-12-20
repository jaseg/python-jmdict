#!/usr/bin/env python3

import lzma
import pickle
from enum import Enum
from collections import namedtuple

class EntryType:
	def __init__(self, desc):
		self.desc = desc

class OtherEntryTypeMixin:
	other = EntryType

class EntryTypes(EntryType, OtherEntryTypeMixin, Enum):
	def __new__(cls, value):
		if type(value) is cls:
			return value
		try:
			if value in cls._value2member_map_:
				return cls._value2member_map_[value]
		except TypeError:
			for member in cls._member_map_.values():
				if member._value_ == value:
					return member
		return cls.other(value)

	ma		= "martial arts term"
	x		= "rude or X-rated term (not displayed in educational software)"
	abbr	= "abbreviation"
	adj_i	= "adjective (keiyoushi)"
	adj_na	= "adjectival nouns or quasi-adjectives (keiyodoshi)"
	adj_no	= "nouns which may take the genitive case particle `no'"
	adj_pn	= "pre-noun adjectival (rentaishi)"
	adj_t	= "`taru' adjective"
	adj_f	= "noun or verb acting prenominally"
	adj		= "former adjective classification (being removed)"
	adv		= "adverb (fukushi)"
	adv_to	= "adverb taking the `to' particle"
	arch	= "archaism"
	ateji	= "ateji (phonetic) reading"
	aux		= "auxiliary"
	aux_v	= "auxiliary verb"
	aux_adj	= "auxiliary adjective"
	buddh	= "Buddhist term"
	chem	= "chemistry term"
	chn		= "children's language"
	col		= "colloquialism"
	comp	= "computer terminology"
	conj	= "conjunction"
	ctr		= "counter"
	derog	= "derogatory"
	eK		= "exclusively kanji"
	ek		= "exclusively kana"
	exp		= "expressions (phrases, clauses, etc.)"
	fam		= "familiar language"
	fem		= "female term or language"
	food	= "food term"
	geom	= "geometry term"
	gikun	= "gikun (meaning) reading"
	hon		= "honorific or respectful (sonkeigo) language"
	hum		= "humble (kenjougo) language"
	iK		= "word containing irregular kanji usage"
	id		= "idiomatic expression"
	ik		= "word containing irregular kana usage"
	int		= "interjection (kandoushi)"
	io		= "irregular okurigana usage"
	iv		= "irregular verb"
	ling	= "linguistics terminology"
	m_sl	= "manga slang"
	male	= "male term or language"
	male_sl	= "male slang"
	math	= "mathematics"
	mil		= "military"
	n		= "noun (common) (futsuumeishi)"
	n_adv	= "adverbial noun (fukushitekimeishi)"
	n_suf	= "noun, used as a suffix"
	n_pref	= "noun, used as a prefix"
	n_t		= "noun (temporal) (jisoumeishi)"
	num		= "numeric"
	oK		= "word containing out-dated kanji"
	obs		= "obsolete term"
	obsc	= "obscure term"
	ok		= "out-dated or obsolete kana usage"
	on_mim	= "onomatopoeic or mimetic word"
	poet	= "poetical term"
	pol		= "polite (teineigo) language"
	pref	= "prefix"
	prn		= "pronoun"
	prt		= "particle"
	physics	= "physics terminology"
	rare	= "rare"
	sens	= "sensitive"
	sl		= "slang"
	suf		= "suffix"
	un		= "unclassified"
	uK		= "word usually written using kanji alone"
	uk		= "word usually written using kana alone"
	v1		= "Ichidan verb"
	v4r		= "Yondan verb with `ru' ending (archaic)"
	v5		= "Godan verb (not completely classified)"
	v5aru	= "Godan verb - -aru special class"
	v5b		= "Godan verb with `bu' ending"
	v5g		= "Godan verb with `gu' ending"
	v5k		= "Godan verb with `ku' ending"
	v5k_s	= "Godan verb - Iku/Yuku special class"
	v5m		= "Godan verb with `mu' ending"
	v5n		= "Godan verb with `nu' ending"
	v5r		= "Godan verb with `ru' ending"
	v5r_i	= "Godan verb with `ru' ending (irregular verb)"
	v5s		= "Godan verb with `su' ending"
	v5t		= "Godan verb with `tsu' ending"
	v5u		= "Godan verb with `u' ending"
	v5u_s	= "Godan verb with `u' ending (special class)"
	v5uru	= "Godan verb - Uru old class verb (old form of Eru)"
	v5z		= "Godan verb with `zu' ending"
	vz		= "Ichidan verb - zuru verb (alternative form of -jiru verbs)"
	vi		= "intransitive verb"
	vk		= "Kuru verb - special class"
	vn		= "irregular nu verb"
	vs		= "noun or participle which takes the aux. verb suru"
	vs_s	= "suru verb - special class"
	vs_i	= "suru verb - irregular"
	kyb		= "Kyoto-ben"
	osb		= "Osaka-ben"
	ksb		= "Kansai-ben"
	ktb		= "Kantou-ben"
	tsb		= "Tosa-ben"
	thb		= "Touhoku-ben"
	tsug	= "Tsugaru-ben"
	kyu		= "Kyuushuu-ben"
	rkb		= "Ryuukyuu-ben"
	vt		= "transitive verb"
	vulg	= "vulgar expression or word"
	nokanji = "Not a true reading of the Kanji"

Entry		= namedtuple('Entry', ['kanji', 'readings', 'translations', 'links'])
Variant		= namedtuple('Variant', ['moji', 'info', 'prio'])
Link		= namedtuple('Link', ['tag', 'description', 'uri'])
Translation	= namedtuple('Translation', ['kanji_limited',
										 'reading_limited',
										 'pos_info',
										 'xrefs',
										 'antonyms',
										 'field_of_use',
										 'misc',
										 'dialect',
										 'info'])

	
if __name__ == '__main__':
	from xml.etree.ElementTree import ElementTree
	from types import SimpleNamespace
	from words import *

	def _load_jmdict(fname):
		with lzma.open(fname, 'rt', encoding='utf-8') as f:
			tree = ElementTree()
			tree.parse(f)
	
		data = set()
		def parse_entry(entry):
			kanji		= [Variant(ele.find('keb').text,
									[EntryType(inf.text) for inf in ele.findall('ke_inf')],
									[pri.text for pri in ele.findall('ke_pri')])
								for ele in entry.findall('k_ele')]
			# FIXME ignoring re_restr for now
			readings	= [Variant(ele.find('reb').text,
									[EntryType(inf.text) for inf in ele.findall('re_inf')] +
									[EntryType.nokanji] if ele.find('re_nokanji') else [],
									[pri.text for pri in ele.findall('re_pri')])
								for ele in entry.findall('r_ele')]
			# NOTE: We are ignoring any <etym>, <bibl> or <audit> elements. The former two are not in use as of the time
			# this code is written (September 2014) and the latter one does not seem interesting at the moment. - jaseg
			links		= [Link(link.find('link_tag').text,
										 link.find('link_desc').text,
										 link.find('link_uri').text)
									 for info in entry.findall('info')
									 for link in info.findall('links')]

			# NOTE: For now, we are ignoring the g_gend attribute as well as the <pri> and <example> elements since
			# these are not used at the time this code is written (September 2014). - jaseg
			# <!ELEMENT sense (s_inf*, lsource*, gloss*)>
			sense_elems		= entry.findall('sense')
			translations = []
			for sense in sense_elems:
				stagk	= [stagk.text for stagk in sense.findall('stagk')]
				stagr	= [stagr.text for stagr in sense.findall('stagr')]
				pos		= [EntryType(pos.text) for pos in sense.findall('pos')]
				xref	= [xref.text for xref in sense.findall('xref')]
				ant		= [ant.text for ant in sense.findall('ant')]
				field	= [field.text for field in sense.findall('field')]
				misc	= [misc.text for misc in sense.findall('misc')]
				dial	= [EntryType(dial.text) for dial in sense.findall('dial')]
				sinf	= [inf.text for inf in sense.findall('s_inf')]
				translations.append(Translation(stagk, stagr, pos, xref, ant, field, misc, dial, sinf))

			return Entry(kanji, readings, translations, links)
		entries = [ parse_entry(entry) for entry in tree.getroot().findall('entry') ]
		mapping = { key.moji: entry for entry in entries for key in entry.kanji+entry.readings }
		return entries,mapping
	
	entries,mapping = _load_jmdict('JMdict.xml.lzma')
	
	with lzma.open('word_data.pickle.lzma', 'wb') as f:
		pickle.dump((entries,mapping), f)
else:
	from words import *
	with lzma.open('word_data.pickle.lzma', 'rb') as f:
		entries,mapping = pickle.load(f)

