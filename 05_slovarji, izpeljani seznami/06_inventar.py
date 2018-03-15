datoteka = open('preberi_inventar.txt')


def preberi_inventar(ime_dat):
    inventar = {}
    for vrstica in ime_dat:
        izdelek, kolicina = vrstica.split('\t')
        inventar[izdelek] = int(kolicina.strip())
    return inventar


inv = preberi_inventar(datoteka)


def zaloga(inventar, artikel):
    return inventar[artikel]
print(zaloga(inv, 'makovka'))


def prodaj(inv, artikel, kolicina):
    inv[artikel] -= kolicina


prodaj(inv, 'makovka', 3)
print(inv)


def preberi_narocilo(ime_dat):
    return preberi_inventar(ime_dat)


nar = preberi_inventar(datoteka)
print(nar)