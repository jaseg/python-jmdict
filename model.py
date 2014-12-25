
from collections import namedtuple
from functools import lru_cache
from itertools import groupby
from operator import itemgetter

# small utility function for generating translation dicts
groupdict = lambda tupgen: {k: [v for _k,v in vs] for k,vs in groupby(sorted(tupgen, key=itemgetter(0)), key=itemgetter(0))}

KATAKANA =
'アイウエオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモヤユヨラリルレロワヰヱヲンヴヷヸヹヺ'
KATAKANA_MAP = {
		'~': 'アイウエオ',
		'k~':  'カキクケコ',
		's~':  'サシスセソ',
		't~':  'タチツテト',
		'n~':  'ナニヌネノ',
		'h~':  'ハヒフヘホ',
		'm~':  'マミムメモ',
		'y~':  'ヤ　ユ　ヨ',
		'r~':  'ラリルレロ',
		'w~':  'ワヰ　ヱヲ',

		'g~':  'ガギグゲゴ',
		'z~':  'ザジズゼゾ',
		'd~':  'ダヂヅデド',
		'b~':  'バビブベボ',
		'p~':  'パピプペポ',

		'~a':  'アカサタナハマヤラワガザダバパ',
		'~i':  'イキシチニヒミ　リヰギジヂビピ',
		'~u':  'ウクスツヌフムユル　グズヅブプ',
		'~e':  'エケセテネヘメ　レヱゲゼデベペ',
		'~o':  'オコソトノホモヨロヲゴゾドボポ',

		'n':  'ン'}

VOICED_KATAKANA_MAP = {
	'カ': 'ガ',
	'キ': 'ギ',
	'ク': 'グ',
	'ケ': 'ゲ',
	'コ': 'ゴ',
	'サ': 'ザ',
	'シ': 'ジ',
	'ス': 'ズ',
	'セ': 'ゼ',
	'ソ': 'ゾ',
	'タ': 'ダ',
	'チ': 'ヂ',
	'ツ': 'ヅ',
	'テ': 'デ',
	'ト': 'ド',
	'ハ': 'バ',
	'ヒ': 'ビ',
	'フ': 'ブ',
	'ヘ': 'ベ',
	'ホ': 'ボ',
	'ウ': 'ヴ',
	'ワ': 'ヷ',
	'ヰ': 'ヸ' ,
	'ヲ': 'ヺ'}

SMALL_KATAKANA = 'ァィゥェォッャュョヮヵヶㇰㇱㇲㇳㇴㇵㇶㇷㇸㇹㇺㇻㇼㇽㇾㇿ'

SMALL_KATAKANA_MAP = {
		'ァ': 'ア',
		'ィ': 'イ',
		'ゥ': 'ウ',
		'ェ': 'エ',
		'ォ': 'オ',
		'ッ': 'ツ',
		'ャ': 'ヤ',
		'ュ': 'ユ',
		'ョ': 'ヨ',
		'ヮ': 'ワ',
		'ヵ': 'カ',
		'ヶ': 'ケ',
		'ㇰ': 'ク',
		'ㇱ': 'シ',
		'ㇲ': 'ス',
		'ㇳ': 'ト',
		'ㇴ': 'ヌ',
		'ㇵ': 'ハ',
		'ㇶ': 'ヒ',
		'ㇷ': 'フ',
		'ㇸ': 'ヘ',
		'ㇹ': 'ホ',
		'ㇺ': 'ム',
		'ㇻ': 'ラ',
		'ㇼ': 'リ',
		'ㇽ': 'ル',
		'ㇾ': 'レ',
		'ㇿ': 'ロ'}

ITERATION_MARKS = 'ーヽヾ'
MORA_REGEX = re.compile('[{.KATAKANA}][{.SMALL_KATAKANA}{.ITERATION_MARKS}]'.format(globals())

# small utility function to split a string into morae
def morae_split(s):



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
    "nokanji" : "Not a true reading of the Kanji",
    # begin of jmndict entry types
    "surname"      : "family or surname",
    "place"        : "place name",
    "unclassified" : "unclassified name",
    "company"      : "company name",
    "product"      : "product name",
    "work"         : "work of art, literature, music, etc. name",
    "malegiven"    : "male given name or forename",
    "femalegiven"  : "female given name or forename",
    "person"       : "full name of a particular person",
    "given"        : "given name or forename, gender not specified",
    "station"      : "railway station",
    "organization" : "organization name",
    "irregular"    : "old or irregular kana form"
    }

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
    "vulg"    : "vulgar",
	# begin of jmndict entry types
    "malegiven"    : "male",
    "femalegiven"  : "female",
    "person"       : "full"}

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


class NameTranslation(namedtuple('NameTranslationBase', ['translations', 'types'])):
    def pretty_print(self, lang='ignored'):
        if self.types:
            return str(self.types)+' '+', '.join(self.translations)
        else:
            return ', '.join(self.translations)

    def __str__(self):
        return self.pretty_print()

KanjiVGEntry = namedtuple('KanjiVGEntry', ['strokes', 'groups'])

KanjidicEntry = namedtuple('KanjidicEntry', [
        'literal',
        'codepoint',
        'radicals',
        'grade',
        'stroke_count',
        'variants',
        'frequency',
        'rad_names',
        'jlpt_level',
        'dic_numbers',
        'query_codes',
        'rms',
        'nanori',
        'decomposition',
        'kanjivg'])
