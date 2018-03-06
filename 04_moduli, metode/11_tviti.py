tviti = ["sandra: Spet ta dež. #dougcajt",
         "berta: @sandra Delaj domačo za #programiranje1",
         "sandra: @berta Ne maram #programiranje1 #krneki",
         "ana: kdo so te @berta, @cilka, @dani? #krneki",
         "cilka: jst sm pa #luft",
         "benjamin: pogrešam ano #zalosten",
         "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


def unikati(s):
    nov = []
    for i in s:
        if not i in nov:
            nov.append(i)
    return nov


print(unikati([1, 3, 2, 1, 1, 3, 2]))


######################################################################

def avtor(tvit):
    return tvit.split(':')[0]


print(avtor("ana: kdo so te @berta, @cilka, @dani? #krneki"))


######################################################################

def vsi_avtorji(tviti):
    return unikati(avtor(tvit) for tvit in tviti)


print(vsi_avtorji(tviti))


######################################################################

def izloci_besedo(beseda):
    izl_beseda = beseda
    for znak in beseda:
        if not znak.isalnum():
            izl_beseda = izl_beseda[1:]
        else:
            break
    for znak in reversed(beseda):
        if not znak.isalnum():
            izl_beseda = izl_beseda[:-1]
        else:
            break
    return izl_beseda


print(izloci_besedo('@janez-novak!!!'))


######################################################################

def se_zacne_z(tvit, c):
    ret = []
    besede = tvit.split(' ')
    for beseda in besede:
        if beseda.startswith(c):
            ret.append(izloci_besedo(beseda))
    return ret


print(se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#"))


######################################################################

def zberi_se_zacne_z(tviti, c):
    ret = []
    for tvit in tviti:
        oseba = se_zacne_z(tvit, c)
        ret += oseba
    return unikati(ret)


print(zberi_se_zacne_z(tviti, "@"))


######################################################################

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')


print(vse_afne(tviti))

######################################################################

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')


print(vsi_hashtagi(tviti))

######################################################################

def vse_osebe(tviti):
    osebe = unikati(vse_afne(tviti) + vsi_avtorji(tviti))
    osebe.sort()
    return osebe


print(vse_osebe(tviti))

######################################################################

def custva(tviti, hashtagi):
    osebe = []
    for tvit in tviti:
        avt = avtor(tvit)
        for hashtag in hashtagi:
            if '#' + hashtag in tvit.split(' '):
                osebe.append(avt)
    return sorted(unikati(osebe))

print(custva(tviti, ['dolgcajt', 'krneki']))

######################################################################

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        besede = tvit.split(' ')
        avt = avtor(tvit)
        if avt == oseba1 and '@'+oseba2 in besede or avt == oseba2 and '@'+oseba1 in besede:
            return True
    return False

print(se_poznata(tviti, 'berta', 'sandra'))