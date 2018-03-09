import collections

banka = [("Ana", 2), ("Berta", 8), ("Ana", 4), ("Berta", -3)]

def bilanca(transakcije, ime):
    skupaj = 0
    for kdo, znesek in transakcije:
        if kdo == ime:
            skupaj += znesek
    return skupaj

print(bilanca(banka, 'Berta'))

############################################################

def klienti(transakcije):
    imena = []
    for kdo, znesek in transakcije:
        if kdo not in imena:
            imena.append(kdo)
    return imena

def najbogatejsi(transakcije):
    osebe = klienti(transakcije)
    stanje = 0
    najbogatejsa_oseba = ''
    for oseba in osebe:
        stanje_novo = bilanca(transakcije, oseba)
        if stanje_novo > stanje:
            stanje = stanje_novo
            najbogatejsa_oseba = oseba
    return najbogatejsa_oseba

print(najbogatejsi(banka))

############################################################

def racunovodja(transakcije):
    knjiga = []
    for kdo, znesek in transakcije:
        for racun in knjiga:
            if racun[0] == kdo:
                racun[1] += znesek
                break
        else:
            knjiga.append([kdo, znesek])
    return knjiga

print(racunovodja(banka))

############################################################

