def mrange(zac, fac, dol):
    sez = [zac]
    for i in range(dol - 1):
        sez.append(zac * fac)
        zac = zac * fac
    return sez

print(mrange(7,4,7))

