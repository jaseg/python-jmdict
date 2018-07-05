#!/usr/bin/env python3

from collections import namedtuple

Endings = namedtuple('Endings', ['v5u', 'v5k', 'v5g', 'v5s', 'v5t', 'v5m', 'v5b', 'v5n', 'v5r', 'v1'])

forms = [
    'plain affirmative',            ['う',                'く',                'ぐ',                'す',                'つ',                'む',                'ぶ',                'ぬ',                'る',                'る']),

    # present tense
    'polite affirmative':           ['います',            'きます',            'ぎます',            'します',            'ちます',            'みます',            'びます',            'にます',            'ります',            'ます']),
    'plain negative':               ['わない',            'かない',            'がない',            'さない',            'たない',            'まない',            'ばない',            'なない',            'らない',            'ない']),
    'polite negative':              ['いません',          'きません',          'ぎません',          'しません',          'ちません',          'みません',          'びません',          'にません',          'りません',          'ません']),
    'curt negative (archaic)':      ['わん',              'かん',              'がん',              'さん',              'たん',              'まん',              'ばん',              'なん',              'らん',              'ん']),
    'polite negative (archaic)':    ['いませぬ',          'きませぬ',          'ぎませぬ',          'しませぬ',          'ちませぬ',          'みませぬ',          'びませぬ',          'にませぬ',          'りませぬ',          'ませぬ']),

    # past tense
    'past tense':                   ['った',              'いた',              'いだ',              'した',              'った',              'んだ',              'んだ',              'んだ',              'った',              'た']),
    'polite affirmative':           ['いました',          'きました',          'ぎました',          'しました',          'ちました',          'みました',          'びました',          'にました',          'りました',          'ました']),
    'plain negative':               ['わなかった',        'かなかった',        'がなかった',        'さなかった',        'たなかった',        'まなかった',        'ばなかった',        'ななかった',        'らなかった',        'なかった']),
    'polite negative':              ['いませんでした',    'きませんでした',    'ぎませんでした',    'しませんでした',    'ちませんでした',    'みませんでした',    'びませんでした',    'にませんでした',    'りませんでした',    'ませんでした']),

    # perfect
    'negative perfect':             ['わず(に)',          'かず(に)',          'がず(に)',          'さず(に)',          'たず(に)',          'まず(に)',          'ばず(に)',          'なず(に)',          'らず(に)',          'ず(に)']),

    # ta form
    'representative':               ['ったり',            'いたり',            'いだり',            'したり',            'ったり',            'んだり',            'んだり',            'んだり',            'ったり',            'たり']),

    # renyoukei
    'conjunctive':                  ['い-',               'き-',               'ぎ-',               'し-',               'ち-',               'み-',               'び-',               'に-',               'り-',               '-']),
    'way of doing':                 ['いかた',            'きかた',            'ぎかた',            'しかた',            'ちかた',            'みかた',            'びかた',            'にかた',            'りかた',            'かた']),

    # te forms
    'te form':                      ['って',              'いて',              'いで',              'して',              'って',              'んで',              'んで',              'んで',              'って',              'て']),
    'te iru':                       ['っている',          'いている',          'いでいる',          'している',          'っている',          'んでいる',          'んでいる',          'んでいる',          'っている',          'ている']),
    'simplified te iru':            ['ってる',            'いてる',            'いでる',            'してる',            'ってる',            'んでる',            'んでる',            'んでる',            'ってる',            'てる']),
    'te aru':                       ['ってある',          'いてある',          'いである',          'してある',          'ってある',          'んである',          'んである',          'んである',          'ってある',          'てある']),
    'simplified te ageru':          ['ったげる',          'いたげる',          'いだげる',          'したげる',          'ったげる',          'んだげる',          'んだげる',          'んだげる',          'ったげる',          'たげる']),
    'te oru':                       ['っておる',          'いておる',          'いでおる',          'しておる',          'っておる',          'んでおる',          'んでおる',          'んでおる',          'っておる',          'ておる']),
    'simplified te oru':            ['っとる',            'いとる',            'いどる',            'しとる',            'っとる',            'んどる',            'んどる',            'んどる',            'っとる',            'とる']),
    'te oku':                       ['っておく',          'いておく',          'いでおく',          'しておく',          'っておく',          'んでおく',          'んでおく',          'んでおく',          'っておく',          'ておく']),
    'simplified te oku':            ['っとく',            'いとく',            'いどく',            'しとく',            'っとく',            'んどく',            'んどく',            'んどく',            'っとく',            'とく']),

    # tai/tageru
    'desire':                       ['いたい',            'きたい',            'ぎたい',            'したい',            'ちたい',            'みたい',            'びたい',            'にたい',            'りたい',            'たい']),
    "other's desire":               ['いたがる',          'きたがる',          'ぎたがる',          'したがる',          'ちたがる',          'みたがる',          'びたがる',          'にたがる',          'りたがる',          'たがる']),

    # pseudo-futurum forms
    'pseudo futurum':               ['おう',              'こう',              'ごう',              'そう',              'とう',              'もう',              'ぼう',              'のう',              'ろう',              'よう']),
    'polite presumptive':           ['うでしょう',        'くでしょう',        'ぐでしょう',        'すでしょう',        'つでしょう',        'むでしょう',        'ぶでしょう',        'ぬでしょう',        'るでしょう',        'るでしょう']),
    'plain presumptive':            ['うだろう',          'くだろう',          'ぐだろう',          'すだろう',          'つだろう',          'むだろう',          'ぶだろう',          'ぬだろう',          'るだろう',          'るだろう']),
    'polite negative presumptive':  ['わないだろう',      'かないだろう',      'がないだろう',      'さないだろう',      'たないだろう',      'まないだろう',      'ばないだろう',      'なないだろう',      'らないだろう',      'ないだろう']),
    'plain negative presumptive':   ['うまい',            'くまい',            'ぐまい',            'すまい',            'つまい',            'むまい',            'ぶまい',            'ぬまい',            'るまい',            'まい']),
    'past presumptive':             ['ったろう',          'いたろう',          'いだろう',          'したろう',          'ったろう',          'んだろう',          'んだろう',          'んだろう',          'った',              'たろう']),

    # izenkei / kateikei
    'hypothetical':                 ['えば',              'けば',              'げば',              'せば',              'てば',              'めば',              'べば',              'ねば',              'れば',              'れば']),
    'past hypothetical':            ['ったら',            'いたら',            'いだら',            'したら',            'ったら',            'んだら',            'んだら',            'んだら',            'ったら',            'たら']),
    'short potential':              ['える',              'ける',              'げる',              'せる',              'てる',              'める',              'べる',              'ねる',              'れる',              '']),

    # saserareru
    'passive':                      ['われる',            'かれる',            'がれる',            'される',            'たれる',            'まれる',            'ばれる',            'なれる',            'られる',            'られる']),
    'causative':                    ['わせる',            'かせる',            'がせる',            'させる',            'たせる',            'ませる',            'ばせる',            'なせる',            'らせる',            'させる']),
    'causative passive':            ['わせられる',        'かせられる',        'がせられる',        'させられる',        'たせられる',        'ませられる',        'ばせられる',        'なせられる',        'らせられる',        'させられる']),

    # commands
    'requesting':                   ['ってください',      'いてください',      'いでください',      'してください',      'ってください',      'んでください',      'んでください',      'んでください',      'ってください',      'てください']),

    'commanding':                   ['え',                'け',                'げ',                'せ',                'て',                'め',                'べ',                'ね',                'れ',                'ろ']),
    'authoritative':                ['いなさい',          'きなさい',          'ぎなさい',          'しなさい',          'ちなさい',          'みなさい',          'びなさい',          'になさい',          'りなさい',          'なさい']),
    'advisory':                     ['',                  '',                  '',                  '',                  '',                  '',                  '',                  '',                  '',                  'よ']),
    'negative request':             ['わないでください',  'かないでください',  'がないでください',  'さないでください',  'たないでください',  'まないでください',  'ばないでください',  'なないでください',  'らないでください',  'ないでください']),
    'negative imperative':          ['うな',              'くな',              'ぐな',              'すな',              'つな',              'むな',              'ぶな',              'ぬな',              'るな',              'るな']),

    # belief about [...]ness
    'looks to be the case':         ['いそう',            'きそう',            'ぎそう',            'しそう',            'ちそう',            'みそう',            'びそう',            'にそう',            'りそう',            'そう']),
    'claimed to be the case':       ['うそう',            'くそう',            'ぐそう',            'すそう',            'つそう',            'むそう',            'ぶそう',            'ぬそう',            'るそう',            'るそう']),
    'apparently the case':          ['うらしい',          'くらしい',          'ぐらしい',          'すらしい',          'つらしい',          'むらしい',          'ぶらしい',          'ぬらしい',          'るらしい',          'るらしい'])]

verb_endings = {'う': 'u',  'く': 'k',  'ぐ': 'g',  'す': 's',  'つ': 't', 'む': 'm',  'ぶ': 'b',  'ぬ': 'n',  'る': 'r'}

var process = function(word, seen, aggregated, entry, i, suffix, j) {
  if(!suffix.trim()) return;
  var re = new RegExp(suffix + "$");
  if (word.match(re)) {
    newword = word.replace(re, verbEndings[j]);
    // special check for する
    if (newword === "す") { newword = "する"; }
    // terminal check for orphan v1
    if (newword === "る") { return; }
    aggregated.push(destep(newword, seen.concat({
      word: newword,
      found: entry.name,
      verbType: verbTypes[j]
    })));
  }
};

def deconjugate(verb):
    for name, endings in forms:
        for i, ending in enumerate(endings):
           if verb.ends_with(ending):
               # FIXME add dict lookup here
               vstem = verb[:-len(ending))
               yield name, ending, vstem + forms['plain affirmative'][i]

def get_v5_subtype(verb):
    return verb_endings[verb[-1]]

def conjugate(verb, vtype=None) {
    vtype = vtype or get_v5_subtype(verb) # FIXME dict lookup
    vstem = verb[:-1]

    for name, endings in forms:
        yield name, vstem+getattr(endings, vtype)