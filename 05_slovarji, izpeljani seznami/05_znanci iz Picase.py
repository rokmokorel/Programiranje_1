datoteka = open('izvoz.xml', mode='r')


for vrstica in datoteka:
    drzava = vrstica.split()[0]
    dobrine = vrstica.split()[1:]
    print('{}\n{}\n'.format(drzava, dobrine))

drzave = {}
produkti = {}
for vrstica in datoteka:
    sez_produktov = vrstica.split()[1:]
    ime_drzave = vrstica.split()[0]
    drzave[ime_drzave] = sez_produktov
    for ime in sez_produktov:
        if ime not in produkti:
            produkti[ime] = [ime_drzave]
        else:
            produkti[ime] += ime_drzave

def kdo_izvaza(produkt):
    return produkti[produkt]

def kaj_izvaza(drzava):
    return drzave[drzava]