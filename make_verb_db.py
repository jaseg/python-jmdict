#!/usr/bin/env python3

import sqlite3
import words
import model

db = sqlite3.connect('verbs.db')

_verbinfo = {'v1', 'v4r', 'v5', 'v5aru', 'v5b', 'v5g', 'v5k', 'v5k_s', 'v5m', 'v5n', 'v5r', 'v5r_i', 'v5s', 'v5t', 'v5u',
        'v5u_s', 'v5uru', 'v5z', 'vk', 'vn', 'vs', 'vs_i', 'vs_s', 'vz'}
verbinfo = { model.EntryType(model.EntryType.LONG[i]) for i in _verbinfo }

def verb_gen():
    for e in words.entries:
        for v in e.translations:
            for i in v.pos_info:
                print(i)
        if any(i in verbinfo for t in e.translations for i in t.pos_info):
           yield e

with db as conn:
    pass
