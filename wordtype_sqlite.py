#!/usr/bin/env python3

import sqlite3

import words


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('sqlite3_out', nargs='?', default='wordtype.sqlite3', help='SQLite3 database file to fill')
    args = parser.parse_args()

    db = sqlite3.connect(args.sqlite3_out)
    with db as conn:
        db.execute('DROP TABLE IF EXISTS wordtypes')
        db.execute('CREATE TABLE wordtypes (kanji, readings, glosses, priority, part_of_speech)')

        for entry in words.entries:
            for kanji in entry.kanji:
                #kanji = ', '.join(variant.moji for variant in entry.kanji)
                for reading in entry.readings:
                    #readings = ', '.join(reading.moji for reading in entry.readings)
                    for translation in entry.translations:
                        glosses = ', '.join(translation.gloss)
                        pos_info = ', '.join(str(e) for e in translation.pos_info)
                        db.execute('INSERT INTO wordtypes VALUES (?, ?, ?, ?)', (kanji.moji, reading.moji, glosses, pos_info))

