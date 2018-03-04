def najdaljsa(s):
    naj = ''
    for beseda in s.split():
        if len(beseda) > len(naj):
            naj = beseda
    return naj
print(najdaljsa('an bam pet podgan'))

#-------------------------------------------------------------------

def podobnost(s1, s2):
    stevec = 0
    for a, b in zip(s1, s2):
        if a == b:
            stevec += 1
    return stevec
print(podobnost('sobota', 'robot'))

#-------------------------------------------------------------------

def sumljive(s):
    sumljive = []
    for beseda in s.split():
            if 'a' in beseda and 'u' in beseda:
                sumljive.append(beseda)
    return sumljive
print(sumljive('Muha pa je rekla: "Tale juha se je pa res prilegla, najlepša huala," in odletela.'))

#-------------------------------------------------------------------

def vsi(xs):
    for i in xs:
        if not i:
            return False
    return True
print(vsi([True, True, False]))

#-------------------------------------------------------------------

def vsaj_eden(xs):
    for i in xs:
        if i:
            return True
    return False
print(vsaj_eden([]))

#-------------------------------------------------------------------

def domine(xs):
    for i in range(len(xs)-1):
        if xs[i][1] != xs[i+1][0]:
            return False
    return True
print(domine([(3, 6), (6, 6), (2, 3)]))

#-------------------------------------------------------------------

def vsote_podseznamov(xs):
    ret = []
    for pod in xs:
        delni = 0
        for i in pod:
            delni += i
        ret.append(delni)
    return ret

print(vsote_podseznamov([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]]))

def vsote_podseznamov_boljse(xs):
    return list(map(sum, xs))

print(vsote_podseznamov_boljse([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]]))

#-------------------------------------------------------------------

def najvecji_podseznam(xs):
    naj = []
    for i in xs:
        if sum(i) > sum(naj):
            naj = i
    return naj
print('naj: ', najvecji_podseznam([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]]))

#-------------------------------------------------------------------

def cezar(s):
    koda = []
    for beseda in s.split():
        bes = ''
        for crka in beseda:
            if 'a' <= crka <= 'w':
                crka = chr(ord(crka) + 3)
                bes += crka
            elif 'x' <= crka <= 'z':
                crka = chr(ord(crka) - 23)
                bes += crka
            else:
                bes += crka
        koda.append(bes)
    return ' '.join(koda)

print(cezar('malica na hribu'))

#-------------------------------------------------------------------

def mrange(start, faktor, dolzina):
    ret = [start]
    for i in range(dolzina - 1):
        ret.append(ret[i] * faktor)
    return ret
print(mrange(7,4,7))

#-------------------------------------------------------------------

def slikaj(f, xs):
    ret = []
    for i in xs:
        ret.append(f(i))
    return ret
print(slikaj(abs, [-5, 8, -3, -1, 3]))


