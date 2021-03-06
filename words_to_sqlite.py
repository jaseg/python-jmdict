#!/usr/bin/env python3

import words

db = sqlite3.connect('words.db')

with db as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS kanji_variants (moji TEXT,'
                                                            'info INTEGER FOREIGN KEY,'
                                                            'prio INTEGER FOREIGN KEY)')
    conn.execute('CREATE TABLE IF NOT EXISTS reading_variants (moji TEXT,'
                                                              'info INTEGER FOREIGN KEY,'
                                                              'prio INTEGER FOREIGN KEY)')

    conn.execute('CREATE TABLE IF NOT EXISTS links (tag TEXT, desc TEXT, uri TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS glosses (gloss TEXT, lang INTEGER)')
    conn.execute('CREATE TABLE IF NOT EXISTS translations (antonyms INTEGER FOREIGN KEY,'
                                                          'pos_info INTEGER')

    conn.execute('CREATE TABLE IF NOT EXISTS prios'
                    '(name TEXT, description TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS infos'
                    '(key TEXT, shortform TEXT, description TEXT)')
    conn.execute('INSERT INTO infos VALUES ?',
        [('abbr',          'abbreviation',                                                  'abbr.'),
         ('adj',           'former adjective classification (being removed)',               'adj.'),
         ('adj_f',         'noun or verb acting prenominally',                              None),
         ('adj_i',         'adjective (keiyoushi)',                                         'adj. verb'),
         ('adj_na',        'adjectival nouns or quasi-adjectives (keiyodoshi)',             'な-adj.'),
         ('adj_no',        'nouns which may take the genitive case particle "no"',          'の-adj.'),
         ('adj_pn',        'pre-noun adjectival (rentaishi)',                               None),
         ('adj_t',         '"taru" adjective',                                              None),
         ('adv',           'adverb (fukushi)',                                              'adverb'),
         ('adv_to',        'adverb taking the "to" particle',                               'と-adverb'),
         ('arch',          'archaism',                                                      None),
         ('ateji',         'ateji (phonetic) reading',                                      None),
         ('aux',           'auxiliary',                                                     None),
         ('aux_adj',       'auxiliary adjective',                                           'aux. adj.'),
         ('aux_v',         'auxiliary verb',                                                'aux. verb'),
         ('buddh',         'Buddhist term',                                                 None),
         ('chem',          'chemistry term',                                                None),
         ('chn',           "children's language", None),
         ('col',           'colloquialism',                                                 None),
         ('comp',          'computer terminology',                                          None),
         ('company',       'company name',                                                  None),
         ('conj',          'conjunction',                                                   None),
         ('ctr',           'counter',                                                       'ctr.'),
         ('derog',         'derogatory',                                                    None),
         ('eK',            'exclusively kanji',                                             None),
         ('ek',            'exclusively kana',                                              None),
         ('exp',           'expressions (phrases, clauses, etc.)',                          'expression'),
         ('fam',           'familiar language',                                             'familiar'),
         ('fem',           'female term or language',                                       'feminine'),
         ('femalegiven',   'female given name or forename',                                 'female'),
         ('food',          'food term',                                                     None),
         ('geom',          'geometry term',                                                 None),
         ('gikun',         'gikun (meaning) reading',                                       None),
         ('given',         'given name or forename, gender not specified',                  None),
         ('hon',           'honorific or respectful (sonkeigo) language',                   'honorific'),
         ('hum',           'humble (kenjougo) language',                                    'humble'),
         ('iK',            'word containing irregular kanji usage',                         None),
         ('id',            'idiomatic expression',                                          'idiomatic'),
         ('ik',            'word containing irregular kana usage',                          None),
         ('int',           'interjection (kandoushi)',                                      'interjection'),
         ('io',            'irregular okurigana usage',                                     None),
         ('irregular',     'old or irregular kana form',                                    None),
         ('iv',            'irregular verb',                                                'irregular verb'),
         ('ksb',           'Kansai-ben',                                                    None),
         ('ktb',           'Kantou-ben',                                                    None),
         ('kyb',           'Kyoto-ben',                                                     None),
         ('kyu',           'Kyuushuu-ben',                                                  None),
         ('ling',          'linguistics terminology',                                       None),
         ('m_sl',          'manga slang',                                                   None),
         ('ma',            'martial arts term',                                             None),
         ('male',          'male term or language',                                         'masculine'),
         ('male_sl',       'male slang',                                                    'male slang'),
         ('malegiven',     'male given name or forename',                                   'male'),
         ('math',          'mathematics',                                                   None),
         ('mil',           'military',                                                      None),
         ('n',             'noun (common) (futsuumeishi)',                                  'noun'),
         ('n_adv',         'adverbial noun (fukushitekimeishi)',                            'adv. noun'),
         ('n_pref',        'noun, used as a prefix',                                        'prefix noun'),
         ('n_suf',         'noun, used as a suffix',                                        'suffix noun'),
         ('n_t',           'noun (temporal) (jisoumeishi)',                                 'temporal noun'),
         ('nokanji',       'Not a true reading of the Kanji',                               None),
         ('num',           'numeric',                                                       'numeric'),
         ('oK',            'word containing out-dated kanji',                               None),
         ('obs',           'obsolete term',                                                 'obsolete'),
         ('obsc',          'obscure term',                                                  'obscure'),
         ('ok',            'out-dated or obsolete kana usage',                              None),
         ('on_mim',        'onomatopoeic or mimetic word',                                  'onomatopoeia'),
         ('organization',  'organization name',                                             None),
         ('osb',           'Osaka-ben',                                                     None),
         ('person',        'full name of a particular person',                              'full'),
         ('physics',       'physics terminology',                                           None),
         ('place',         'place name',                                                    None),
         ('poet',          'poetical term',                                                 'poetical'),
         ('pol',           'polite (teineigo) language',                                    'polite'),
         ('pref',          'prefix',                                                        None),
         ('prn',           'pronoun',                                                       None),
         ('product',       'product name',                                                  None),
         ('prt',           'particle',                                                      None),
         ('rare',          'rare',                                                          None),
         ('rkb',           'Ryuukyuu-ben',                                                  None),
         ('sens',          'sensitive',                                                     None),
         ('sl',            'slang',                                                         None),
         ('station',       'railway station',                                               None),
         ('suf',           'suffix',                                                        None),
         ('surname',       'family or surname',                                             None),
         ('thb',           'Touhoku-ben',                                                   None),
         ('tsb',           'Tosa-ben',                                                      None),
         ('tsug',          'Tsugaru-ben',                                                   None),
         ('uK',            'word usually written using kanji alone',                        'usually kanji'),
         ('uk',            'word usually written using kana alone',                         'usually kana'),
         ('un',            'unclassified',                                                  None),
         ('unclassified',  'unclassified name',                                             None),
         ('v1',            'Ichidan verb',                                                  'ichidan'),
         ('v4r',           'Yondan verb with "ru" ending (archaic)',                        'yondan 〜る'),
         ('v5',            'Godan verb (not completely classified)',                        'godan'),
         ('v5aru',         'Godan verb - -aru special class',                               'godan 〜ある'),
         ('v5b',           'Godan verb with "bu" ending',                                   'godan〜ぶ'),
         ('v5g',           'Godan verb with "gu" ending',                                   'godan 〜ぐ'),
         ('v5k',           'Godan verb with "ku" ending',                                   'godan 〜く'),
         ('v5k_s',         'Godan verb - Iku/Yuku special class',                           'godan 〜いく／ゆく'),
         ('v5m',           'Godan verb with "mu" ending',                                   'godan 〜む'),
         ('v5n',           'Godan verb with "nu" ending',                                   'godan 〜ぬ'),
         ('v5r',           'Godan verb with "ru" ending',                                   'godan 〜る'),
         ('v5r_i',         'Godan verb with "ru" ending (irregular verb)',                  'godan 〜る (irregular)'),
         ('v5s',           'Godan verb with "su" ending',                                   'godan 〜す'),
         ('v5t',           'Godan verb with "tsu" ending',                                  'godan 〜つ'),
         ('v5u',           'Godan verb with "u" ending',                                    'godan 〜う'),
         ('v5u_s',         'Godan verb with "u" ending (special class)',                    'godan 〜う (special)'),
         ('v5uru',         'Godan verb - Uru old class verb (old form of Eru)',             None),
         ('v5z',           'Godan verb with "zu" ending',                                   'godan 〜ず'),
         ('vi',            'intransitive verb',                                             'intransitive'),
         ('vk',            'Kuru verb - special class',                                     'くる-verb (special)'),
         ('vn',            'irregular nu verb',                                             '〜ぬ-verb (irregular)'),
         ('vs',            'noun or participle which takes the aux. verb suru',             'する-verb'),
         ('vs_i',          'suru verb - irregular',                                         'する-verb (irregular)'),
         ('vs_s',          'suru verb - special class',                                     'する-verb (special)'),
         ('vt',            'transitive verb',                                               'transitive'),
         ('vulg',          'vulgar expression or word',                                     'vulgar'),
         ('vz',            'Ichidan verb - zuru verb (alternative form of -jiru verbs)',    None),
         ('work',          'work of art, literature, music, etc. name',                     None),
         ('x',             'rude or X-rated term (not displayed in educational software)',  None)] )

for entry in words.entries:
    db.

