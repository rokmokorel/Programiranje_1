import random

razpored = ["a4", "c7", "d2"]

stolpci = "abcdefgh"
vrstice = "12345678"


# ********************************* ZA OCENO 6 *********************************

def stolpec_prost(stolpec, razpored):
    for i in razpored:
        if i[0] == stolpec:
            return False
    return True


print(stolpec_prost('c', razpored))


def prosti_stolpci(raz):
    pr_stolpci = []
    for i in stolpci:
        if stolpec_prost(i, raz):
            pr_stolpci.append(i)
    return pr_stolpci


print(prosti_stolpci(razpored))


def prost_stolpec(raz):
    for i in stolpci:
        if stolpec_prost(i, raz):
            return i
            break


print(prost_stolpec([]))


# ********************************* REŠEVANJE ZA 7 *********************************
def napada(polje1, polje2):
    return polje1[0] == polje2[0] or polje1[1] == polje2[1] or abs(ord(polje1[0]) - ord(polje2[0])) == abs(ord(polje1[1]) - ord(polje2[1]))
print('a4 napada a7: ', napada("a4", "a7"))


def napadajo(polje, razpored):
    sez_napadajo = []
    for i in razpored:
        if napada(polje, i):
            sez_napadajo.append(i)
    return sez_napadajo
print(napadajo("g8", ["a4", "c7", "d2"]))


def napadeno(polje, razpored):
    if napadajo(polje, razpored) == []:
        return False
    else:
        return True
print(napadeno("g8", ["a4", "c7", "d2"]))


# ********************************* REŠEVANJE ZA 8 *********************************
def prosto_v_stolpcu(stolpec, postavitev):
    prosto = []
    for vrstica in vrstice:
        if not napadeno(stolpec + vrstica, postavitev):
            prosto.append(stolpec + vrstica)
    return prosto
print(prosto_v_stolpcu("a", ["b4", "c7", "d2"]))

def prosto_polje(postavitev):
    for stolpec in stolpci:
        for vrstica in vrstice:
            if not napadeno(stolpec + vrstica, postavitev):
                return stolpec+vrstica
print(prosto_polje(["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]))

# ********************************* REŠEVANJE ZA 9 *********************************
def napadajoce_se(razpored):
    napadajoci_pari = []
    for i, kraljica1 in enumerate(razpored):
        for kraljica2 in razpored[:i]:
            if napada(kraljica1,kraljica2):
                napadajoci_pari.append((kraljica1,kraljica2))
    return napadajoci_pari
print(napadajoce_se(["a4", "b1", "b7"]))

def legalna(postavitev):
    if len(postavitev) == 8:
        if napadajoce_se(postavitev) == []:
            return True
        else:
            return False
    else:
        return False
print(legalna(["a4", "b1", "c5", "d8", "e2", "f7", "g3", "h3"]))

# ********************************* REŠEVANJE ZA 10 *********************************
def sestavi_sam():
    razpored = [stolpci[random.randint(0,7)]+vrstice[random.randint(0,7)]]
    print(razpored)
    x = y = 0
    while len(razpored) < 4:
        for stolpec in stolpci[x:]:
            x += 1
            for vrstica in vrstice[y:]:
                y += 1
                spr = stolpec + vrstica
                switch = False
                for i in razpored:
                    if napada(i, spr):
                        switch = True
                if switch == False:
                    razpored.append(spr)
                    print('bum')
    return razpored
#print(sestavi_sam())