datoteka = open('izvoz.xml', mode='r')
'''
for vrstica in datoteka:
    drzava = vrstica.split('\t ')[0]
    dobrine = vrstica.split('\t ')[1].split(', ')
    dobrine[-1] = dobrine[-1].strip('\n')
    print('{}\n{}\n'.format(drzava, dobrine))
'''

drzave = {}
produkti = {}
for vrstica in datoteka:
    ime_drzave = vrstica.split('\t ')[0]
    sez_produktov = vrstica.split('\t ')[1].split(', ')
    sez_produktov[-1] = sez_produktov[-1].strip('\n')

    drzave[ime_drzave] = sez_produktov
    for ime in sez_produktov:
        if ime not in produkti:
            produkti[ime] = [ime_drzave]
        else:
            produkti[ime].append(ime_drzave)

def kdo_izvaza(produkt):
    return produkti[produkt]

def kaj_izvaza(drzava):
    return drzave[drzava]

print(kaj_izvaza('Puerto Rico'))
print(kdo_izvaza('rum'))