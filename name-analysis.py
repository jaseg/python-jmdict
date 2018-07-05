# coding: utf-8

import words
words.mapping['ぶるぶる']
[e for e in words.entries if words.EntryType('on_mim') in e.misc]
[e for e in words.entries if any(words.EntryType('on_mim') in t.misc for t in e.translations)]
len([e for e in words.entries if any(words.EntryType('on_mim') in t.misc for t in e.translations)])
kana = list('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞだでどばびぶべぼ')
kana_comp = [a+b for a in 'きしちにひみりぎじび' for b in 'ゃゅょ']
all_kana = kana + kana_comp
comb = [ a+b+a+b for a in all_kana for b in all_kana]
set(comb) & words.mapping.keys()
len(set(comb) & words.mapping.keys())
len(set(comb) & words.mapping.keys())/len(comb)*100
comb_red = [ a+b+a+b for a in kana[5:] for b in kana[5:]]
len(set(comb_ret) & words.mapping.keys())/len(comb_ret)*100
len(set(comb_ree) & words.mapping.keys())/len(comb_red)*100
len(set(comb_red) & words.mapping.keys())/len(comb_red)*100
comb_red2 = [ a+b+a+b for a in kana for b in kana]
len(set(comb_red2) & words.mapping.keys())/len(comb_red2)*100
kana = list('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞだでどばびぶべぼぱぴぷぺぽ')
comb_red2 = [ a+b+a+b for a in kana for b in kana]
comb_red = [ a+b+a+b for a in kana[5:] for b in kana[5:]]
comb = [ a+b+a+b for a in all_kana for b in all_kana]
len(set(comb) & words.mapping.keys())/len(comb)*100
len(set(comb_red) & words.mapping.keys())/len(comb_red)*100
len(set(comb_red2) & words.mapping.keys())/len(comb_red2)*100
dakuon_map = dict(zip('がぎぐげござじずぜぞだでどばびぶべぼぱぴぷぺぽ', 'かきくけこさしすせそたてとはひふへほはひっふへほ'))
undakuon = lambda k: dakuon_map.get(k, k)
undakuon('か')
undakuon('だ')
u = undakuon
a,b* = 'abc')
a,b* = 'abc'
b
a,b* = 'abc'
a,*b = 'abc'
b
a,*b = 'ab'
b
a,*b = 'a'
b
[ a+b+a+b for a,b,c,d,r* in words.mapping.keys if not r and u(a) == u(c) and u(b) == u(d) ]
len([ a+b+a+b for a,b,c,d,*r in words.mapping.keys if not r and u(a) == u(c) and u(b) == u(d) ])
len({ a+b+c+d for a,b,c,d,*r in words.mapping.keys() if not r and u(a) == u(c) and u(b) == u(d) })
len({ a+b+c+d for a,b,c,d in (w for w in words.mapping.keys() if len(w) == 4) if u(a) == u(c) and u(b) == u(d) })
len({ a+b+c+d for a,b,c,d in (w for w in words.mapping.keys() if len(w) == 4) if u(a) == u(c) and u(b) == u(d) })
s = { a+b+c+d for a,b,c,d in (w for w in words.mapping.keys() if len(w) == 4) if u(a) == u(c) and u(b) == u(d) }
import collections
collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s])
s = { a+b+c+d for a,b,c,d in (w for w in words.mapping.keys() if len(w) == 4) if u(a) == u(c) and u(b) == u(d) and a in kana_all and b in kana_all }
s = { a+b+c+d for a,b,c,d in (w for w in words.mapping.keys() if len(w) == 4) if u(a) == u(c) and u(b) == u(d) and a in kana_all and b in kana_all }
s = { a+b+c+d for a,b,c,d in (w for w in words.mapping.keys() if len(w) == 4) if u(a) == u(c) and u(b) == u(d) and a in kana and b in kana }
collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s])
list(collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]))
collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s])
collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common()
collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common()
get_ipython().magic('cd ../')
get_ipython().magic('cd ../../misc')
get_ipython().magic('cd ../meta')
get_ipython().magic('cd ../../')
get_ipython().magic('cd meta')
get_ipython().magic('cd stats/')
get_ipython().magic('ls ')
import stats
stats.pretty_histogram
get_ipython().magic('pinfo stats.pretty_histogram')
collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common()
stats.pretty_histogram(collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common())
collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common(5)
[a for a,_b in collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common(5)]
[a for a,_b in collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common(5)]
combl = lambda coll: [ a+b+a+b for a in coll for b in coll]
combl((a for a,_b in collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common(5)))
combl((a for a,_b in collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common(5)))
combl([a for a,_b in collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common(5)])
topn = lambda n: combl([a for a,_b in collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]).most_common(n)])
perc = lambda st: len(set(st) & words.mapping.keys())/len(st)*100
perc(topn(5))
perc(topn(10))
perc(topn(None))
perc(topn(None))
perc(topn(None))
perc(topn(None))
knum = len(collections.Counter([a for a,b,c,d in s] + [b for a,b,c,d in s]))
knum
len(kana)
perc(topn(None))
stats.pretty_histogram( [(i, perc(topn(i))) for i in range(len(kana))] )
perc = lambda st: len(set(st) & words.mapping.keys())/len(st)*100 if len(st) > 0 else 0
stats.pretty_histogram( [(i, perc(topn(i))) for i in range(len(kana))] )
perc = lambda st: len(set(st) & words.mapping.keys())/len(st)*100 if len(st) > 0 else 0
stats.pretty_histogram( [(i, perc(topn(i))) for i in range(1,len(kana)+1)] )
len(topn(12)
)
len(topn(12))
len(topn(33))
len(topn(45))
45**2
get_ipython().magic('pinfo %save')
get_ipython().magic('save onomatopoeia.ipy')
get_ipython().magic('save onomatopoeia.ipy 0-100')
get_ipython().magic('cd ../../')
get_ipython().magic('cd res/dict/python-jmdict')
get_ipython().magic('ls ')
get_ipython().magic('cd ref/dict/python-jmdict/')
import name
import names
names.mapping
last = collections.Counter( [ c for a,b,c in (n for n in names.mapping if len(n) == 3) if a in all_kana and b in all_kana and c in all_kana ] )
len(last)
last
histogram(last)
stats.pretty_histogram(last)
stats.pretty_histogram(last.most_common())
stats.pretty_histogram(last.most_common(5))
perc = lambda st: len(set(st) & names.mapping.keys())/len(st)*100 if len(st) > 0 else 0
combl = lambda coll, e: [ a+b+e for a in coll for b in coll]
topn = lambda e: combl(all_kana, e)
stats.pretty_histogram( [(i, perc(topn(e))) for e in topn(10)] )
stats.pretty_histogram( [(e, perc(topn(e))) for e in topn(10)] )
stats.pretty_histogram( [(e, perc(topn(e))) for e in topn(10)] )
histogram(last)
stats.pretty_histogram(last.most_common(5))
stats.pretty_histogram( [(e, perc(topn(e))) for e,_n in last.most_common(10)] )
set(combl(all_kana, 'き')) & names.mapping.keys()
set(combl(all_kana, 'の')) & names.mapping.keys()
set(combl(all_kana, 'い')) & names.mapping.keys()
names.mapping['のふい']
names.mapping[']
names.mapping['よへい']
perc = lambda st: len(set(st) & gset)/len(st)*100 if len(st) > 0 else 0
gset
gset = { r for n in names.entries for r in n.readings if names.EntryType('given') in e.types }
gset = { r for e in names.entries for r in e.readings if names.EntryType('given') in e.types }
gset = { r for e in names.entries for r in e.readings if any( names.EntryType('given') in t.types for t in e.translations) }
len(gset)
len(gset)
gset = { r for e in names.entries for r in e.readings if all( names.EntryType('given') not in t.types for t in e.translations) }
len(gset)
gset = { r for e in names.entries for r in e.readings if names.EntryType('given') in e.types }
gset = { r for e in names.entries for r in e.readings if any( names.EntryType('given') in t.types for t in e.translations) }
len(gset)
perc = lambda st: len(set(st) & gset)/len(st)*100 if len(st) > 0 else 0
set(combl(all_kana, 'い')) & names.mapping.keys()
stats.pretty_histogram( [(e, perc(topn(e))) for e,_n in last.most_common(10)] )
perc = lambda st: len(set(st) & gset)/len(st)*100 if len(st) > 0 else 0
stats.pretty_histogram( [(e, perc(topn(e))) for e,_n in last.most_common(10)] )
stats.pretty_histogram( [(e, perc(topn(e))) for e,_n in last.most_common(10)] )
stats.pretty_histogram( [(e, perc(topn(e))) for e,_n in last.most_common(10)] )
topn = lambda e: combl(all_kana, e)
combl = lambda coll: [ a+b for a in coll for b in coll]
topn = lambda: combl(all_kana)
perc(topn())
topn = lambda e: combl(all_kana, e)
combl = lambda coll, e: [ a+e for a in coll]
topn = lambda e: combl(all_kana, e)
last2 = collections.Counter( [ c for a,c in (n for n in names.mapping if len(n) == 2) if a in all_kana and c in all_kana ] )
stats.pretty_histogram( [(e, perc(topn(e))) for e,_n in last2.most_common(10)] )
stats.pretty_histogram( [(e, perc(topn(e))) for e,_n in last2.most_common()] )
get_ipython().magic('save name-analysis.py')
get_ipython().magic('save name-analysis.py 0 160')
