#!/usr/bin/env python3
# This is a helper script for the romaji project

import sys
from itertools import groupby

import names

not_found = 0
for line in open('/home/user/toys/romaji/cities_names'):
    kanji, hepburn = line.strip().split()
    try:
        entries = names.mapping[kanji]
    except KeyError:
        try:
            entries = names.mapping[kanji[:-1]] # cut last kanji (-shi, -ku etc.)
        except KeyError:
            print(f'Not found: {kanji}', file=sys.stderr)
            print(f'{kanji}\t{hepburn}\tNone')
            not_found += 1
            continue
    readings = [k for k, g in groupby(sorted([reading for entry in entries for reading in entry.readings]))]
    print(f'{kanji}\t{hepburn}\t{",".join(readings)}')

print(f'Total not found: {not_found}', file=sys.stderr)
