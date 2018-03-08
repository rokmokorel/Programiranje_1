############################################################ slovarji
stevilke = {"Ana": "041 310239", "Berta": "040 318319", "Cilka": "041 103194", "Dani": "040 193831",
            "Eva": "051 123123", "Fanči": "040 135367", "Helga": "+49 175 4728 475"}

print(stevilke['Ana'])

'''
for ime in stevilke:
    print(ime, ': ', stevilke[ime])
'''
############################################################ izpis

print(stevilke.items())

for ime, stevilka in stevilke.items():
    print(ime, ': ', stevilka)

############################################################ uporaba

stevke = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def kronogram(s):
    v = 0
    for c in s:
        if c in stevke:
            v += stevke[c]
    return v

def kronogram_boljse(s):
    v = 0
    for c in s:
        v += stevke.get(c, 0)
    return v

napis = 'CVIVS IN HOC RENOVATA LOCO PIA FVLGET IMAGO SIS CVSTOS POPVLI SANCTE IACOBE TVI'

print(kronogram(napis))
print(kronogram_boljse(napis))

############################################################ uporaba
# igralna kocka

meti = [4, 4, 4, 3, 2, 3, 5, 3, 3, 4, 6, 6, 6, 1, 3,
        6, 6, 4, 1, 4, 6, 1, 4, 4, 4, 6, 4, 6, 5, 5, 6, 6, 2, 4, 4, 6,
        3, 2, 6, 1, 3, 6, 3, 2, 6, 6, 4, 6, 4, 2, 4, 4, 1, 1, 6, 2, 6,
        6, 4, 3, 4, 2, 6, 5, 6, 3, 2, 5, 1, 5, 3, 6, 4, 6, 2, 2, 4, 1,
        4, 4, 3, 1, 4, 2, 1, 3, 1, 4, 6, 1, 1, 3, 4, 1, 4, 3, 2, 4, 6, 6]

# štetje z seznami(slabo)
kolikokrat = [0] * 6
for met in meti:
    kolikokrat[met-1] += 1
print(kolikokrat)

# štetje s slovarji
kolikokrat_s = {}
for met in meti:
    if met not in kolikokrat_s:
        kolikokrat_s[met] = 0
    kolikokrat_s[met] += 1
print(kolikokrat_s.items())

# uporaba 'podatkovnega tipa' razreda defaultdict in Counter
import collections

kolikokrat_dic = collections.defaultdict(int)
for met in meti:
    kolikokrat_dic[met] += 1

kolikokrat_dic2 = collections.Counter(meti)
print(kolikokrat_dic2)

# kronogram
print(collections.Counter(napis))
def kronogram_slovar(s):
    crke = collections.Counter(s)
    return crke['I'] + crke['V']*5 + crke['X']*10 + \
           crke['L']*50 + crke['C']*100 + crke['D']*500 + crke['M']*1000
print(kronogram_slovar(napis))

# zapis imen datotek
import os

datoteke = {}
for ime in os.listdir(dir):
    konc = os.path.splittext(ime)[1]
    if not konc in datoteke:
        datoteke[konc] = set()
    datoteke[konc].add(ime)

datoteke = collections.defaultdict(set)
for ime in os.listdir(dir):
    konc = os.path.splitext(ime)[1]
    datoteke[konc].add(ime)
