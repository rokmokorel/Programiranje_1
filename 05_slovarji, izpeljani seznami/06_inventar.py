datoteka = open('preberi_inventar.txt')


def preberi_inventar(ime_dat):
    inventar = {}
    for vrstica in ime_dat:
        izdelek, kolicina = vrstica.split('\t')
        inventar[izdelek] = int(kolicina.strip())
    return inventar

print(preberi_inventar(datoteka))


'''
def zaloga(inventar, artikel):
    return inventar[artikel]
'''