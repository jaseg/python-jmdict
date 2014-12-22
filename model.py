
from collections import namedtuple
from functools import lru_cache


class EntryType:
    @lru_cache(None)
    def __new__(cls, desc):
        return super(EntryType, cls).__new__(cls)

    def __getnewargs__(self):
        return (self.short,)

    def __init__(self, desc):
        self.desc = desc
        self.short = type(self).SHORT.get(desc, 'other')
        self.medium = type(self).MEDIUM.get(self.short, self.desc)

    def __repr__(self):
        if self.short != "other":
            return self.short
        else:
            return "other: " + self.desc

    LONG = {
    "ma"      : "martial arts term",
    "x"       : "rude or X-rated term (not displayed in educational software)",
    "abbr"    : "abbreviation",
    "adj_i"   : "adjective (keiyoushi)",
    "adj_na"  : "adjectival nouns or quasi-adjectives (keiyodoshi)",
    "adj_no"  : "nouns which may take the genitive case particle `no'",
    "adj_pn"  : "pre-noun adjectival (rentaishi)",
    "adj_t"   : "`taru' adjective",
    "adj_f"   : "noun or verb acting prenominally",
    "adj"     : "former adjective classification (being removed)",
    "adv"     : "adverb (fukushi)",
    "adv_to"  : "adverb taking the `to' particle",
    "arch"    : "archaism",
    "ateji"   : "ateji (phonetic) reading",
    "aux"     : "auxiliary",
    "aux_v"   : "auxiliary verb",
    "aux_adj" : "auxiliary adjective",
    "buddh"   : "Buddhist term",
    "chem"    : "chemistry term",
    "chn"     : "children's language",
    "col"     : "colloquialism",
    "comp"    : "computer terminology",
    "conj"    : "conjunction",
    "ctr"     : "counter",
    "derog"   : "derogatory",
    "eK"      : "exclusively kanji",
    "ek"      : "exclusively kana",
    "exp"     : "expressions (phrases, clauses, etc.)",
    "fam"     : "familiar language",
    "fem"     : "female term or language",
    "food"    : "food term",
    "geom"    : "geometry term",
    "gikun"   : "gikun (meaning) reading",
    "hon"     : "honorific or respectful (sonkeigo) language",
    "hum"     : "humble (kenjougo) language",
    "iK"      : "word containing irregular kanji usage",
    "id"      : "idiomatic expression",
    "ik"      : "word containing irregular kana usage",
    "int"     : "interjection (kandoushi)",
    "io"      : "irregular okurigana usage",
    "iv"      : "irregular verb",
    "ling"    : "linguistics terminology",
    "m_sl"    : "manga slang",
    "male"    : "male term or language",
    "male_sl" : "male slang",
    "math"    : "mathematics",
    "mil"     : "military",
    "n"       : "noun (common) (futsuumeishi)",
    "n_adv"   : "adverbial noun (fukushitekimeishi)",
    "n_suf"   : "noun, used as a suffix",
    "n_pref"  : "noun, used as a prefix",
    "n_t"     : "noun (temporal) (jisoumeishi)",
    "num"     : "numeric",
    "oK"      : "word containing out-dated kanji",
    "obs"     : "obsolete term",
    "obsc"    : "obscure term",
    "ok"      : "out-dated or obsolete kana usage",
    "on_mim"  : "onomatopoeic or mimetic word",
    "poet"    : "poetical term",
    "pol"     : "polite (teineigo) language",
    "pref"    : "prefix",
    "prn"     : "pronoun",
    "prt"     : "particle",
    "physics" : "physics terminology",
    "rare"    : "rare",
    "sens"    : "sensitive",
    "sl"      : "slang",
    "suf"     : "suffix",
    "un"      : "unclassified",
    "uK"      : "word usually written using kanji alone",
    "uk"      : "word usually written using kana alone",
    "v1"      : "Ichidan verb",
    "v4r"     : "Yondan verb with `ru' ending (archaic)",
    "v5"      : "Godan verb (not completely classified)",
    "v5aru"   : "Godan verb - -aru special class",
    "v5b"     : "Godan verb with `bu' ending",
    "v5g"     : "Godan verb with `gu' ending",
    "v5k"     : "Godan verb with `ku' ending",
    "v5k_s"   : "Godan verb - Iku/Yuku special class",
    "v5m"     : "Godan verb with `mu' ending",
    "v5n"     : "Godan verb with `nu' ending",
    "v5r"     : "Godan verb with `ru' ending",
    "v5r_i"   : "Godan verb with `ru' ending (irregular verb)",
    "v5s"     : "Godan verb with `su' ending",
    "v5t"     : "Godan verb with `tsu' ending",
    "v5u"     : "Godan verb with `u' ending",
    "v5u_s"   : "Godan verb with `u' ending (special class)",
    "v5uru"   : "Godan verb - Uru old class verb (old form of Eru)",
    "v5z"     : "Godan verb with `zu' ending",
    "vz"      : "Ichidan verb - zuru verb (alternative form of -jiru verbs)",
    "vi"      : "intransitive verb",
    "vk"      : "Kuru verb - special class",
    "vn"      : "irregular nu verb",
    "vs"      : "noun or participle which takes the aux. verb suru",
    "vs_s"    : "suru verb - special class",
    "vs_i"    : "suru verb - irregular",
    "kyb"     : "Kyoto-ben",
    "osb"     : "Osaka-ben",
    "ksb"     : "Kansai-ben",
    "ktb"     : "Kantou-ben",
    "tsb"     : "Tosa-ben",
    "thb"     : "Touhoku-ben",
    "tsug"    : "Tsugaru-ben",
    "kyu"     : "Kyuushuu-ben",
    "rkb"     : "Ryuukyuu-ben",
    "vt"      : "transitive verb",
    "vulg"    : "vulgar expression or word",
    "nokanji" : "Not a true reading of the Kanji"}

    MEDIUM = {
    "abbr"    : "abbr.",
    "adj_i"   : "adj. verb",
    "adj_na"  : "な-adj.",
    "adj_no"  : "の-adj.",
    "adj"     : "adj.",
    "adv"     : "adverb",
    "adv_to"  : "と-adverb",
    "aux_v"   : "aux. verb",
    "aux_adj" : "aux. adj.",
    "ctr"     : "ctr.",
    "exp"     : "expression",
    "fam"     : "familiar",
    "fem"     : "feminine",
    "hon"     : "honorific",
    "hum"     : "humble",
    "id"      : "idiomatic",
    "int"     : "interjection",
    "iv"      : "irregular verb",
    "male"    : "masculine",
    "male_sl" : "male slang",
    "n"       : "noun",
    "n_adv"   : "adv. noun",
    "n_suf"   : "suffix noun",
    "n_pref"  : "prefix noun",
    "n_t"     : "temporal noun",
    "num"     : "numeric",
    "obs"     : "obsolete",
    "obsc"    : "obscure",
    "on_mim"  : "onomatopoeia",
    "poet"    : "poetical",
    "pol"     : "polite",
    "uK"      : "usually kanji",
    "uk"      : "usually kana",
    "v1"      : "ichidan",
    "v4r"     : "yondan 〜る",
    "v5"      : "godan",
    "v5aru"   : "godan 〜ある",
    "v5b"     : "godan〜ぶ",
    "v5g"     : "godan 〜ぐ",
    "v5k"     : "godan 〜く",
    "v5k_s"   : "godan 〜いく／ゆく",
    "v5m"     : "godan 〜む",
    "v5n"     : "godan 〜ぬ",
    "v5r"     : "godan 〜る",
    "v5r_i"   : "godan 〜る (irregular)",
    "v5s"     : "godan 〜す",
    "v5t"     : "godan 〜つ",
    "v5u"     : "godan 〜う",
    "v5u_s"   : "godan 〜う (special)",
    "v5z"     : "godan 〜ず",
    "vi"      : "intransitive",
    "vk"      : "くる-verb (special)",
    "vn"      : "〜ぬ-verb (irregular)",
    "vs"      : "する-verb",
    "vs_s"    : "する-verb (special)",
    "vs_i"    : "する-verb (irregular)",
    "vt"      : "transitive",
    "vulg"    : "vulgar"}

    SHORT = { v: k for k,v in LONG.items() }

class Entry(namedtuple('EntryBase', ['kanji', 'readings', 'translations', 'links'])):
	def pretty_print(self, newlines=False, lang='eng'):
		tlist = lambda ts: ('\n  ' if newlines else '; ').join('{}. {}'.format(i+1, t.pretty_print(lang)) for i,t in enumerate(ts))
		vlist = lambda vs: ', '.join(str(v) for v in vs)
		vs = '{} ({})'.format(vlist(self.kanji), vlist(self.readings)) if self.kanji else vlist(self.readings)
		return '{}:{}{}'.format(vs, '\n  ' if newlines else ' ', tlist(self.translations))

	def __str__(self):
		return self.pretty_print()

class Variant(namedtuple('VariantBase', ['moji', 'info', 'prio'])):
	def pretty_print(self):
		if self.info:
			return '{0.moji} {0.info}'.format(self)
		else:
			return self.moji

	def __str__(self):
		return self.pretty_print()

class Link(namedtuple('LinkBase', ['tag', 'description', 'uri'])):
	pass

class Translation(namedtuple('TranslationBase', ['gloss',
                                         'gloss_dict',
                                         'kanji_limited',
                                         'reading_limited',
                                         'pos_info',
                                         'xrefs',
                                         'antonyms',
                                         'field_of_use',
                                         'misc',
                                         'dialect',
										 'info'])):
	@property
	def usage_info(self):
		return self.pos_info + self.misc

	def pretty_print(self, lang='eng'):
		if self.usage_info:
			return str(self.usage_info)+' '+', '.join(self.gloss_dict[lang])
		else:
			return ', '.join(self.gloss_dict[lang])

	def __str__(self):
		return self.pretty_print()


