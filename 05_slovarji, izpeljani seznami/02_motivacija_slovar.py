import collections

banka = [("Ana", 2), ("Berta", 8), ("Ana", 4), ("Berta", -3)]


############################################################

def bilanca(transakcije, ime):
    stanje = collections.defaultdict(int)
    for oseba, znesek in transakcije:
        if oseba == ime:
            stanje[oseba] += znesek
    return stanje


print(bilanca(banka, 'Ana'))


############################################################

def klienti(transakcije):
    imena = []
    for ime, znesek in transakcije:
        if ime not in imena:
            imena.append(ime)
    return imena


print(klienti(banka))


############################################################

def racunovodja(transakcije):
    knjiga = collections.defaultdict(int)
    for ime, znesek in transakcije:
        knjiga[ime] += znesek
    return knjiga


print(racunovodja(banka))


############################################################

def najbogatejsi(transakcije):
    knjiga = racunovodja(transakcije)
    naj, naj_znesek = '', 0
    for ime in knjiga:
        if knjiga[ime] > naj_znesek:
            naj = ime
            naj_znesek = knjiga[ime]
    return naj
print(najbogatejsi(banka))