def sekunde(s):
    h, m, s = s.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


print(sekunde('30:20:10'))


def iz_sekund(s):
    h = s // 3600
    m = (s // 60) % 60
    s = s % 60
    return ':'.join([str(h), str(m), str(s)])


print(iz_sekund(4500))


def podatki(s):
    uvr, st, prim, ime, let, dr, vc, kc = s.split(' ')
    return ime, int(let), sekunde(vc), sekunde(kc)


print(podatki('1 14895 ROMAN SONJA 1979 SLO 0:16:10 0:32:20'))

def pospesek(vrstice):
    uvr, st, prim, ime, let, dr, vc, kc = vrstice.split(' ')
    return (sekunde(kc) - sekunde(vc)) / sekunde(vc)

print(pospesek('1 14895 ROMAN SONJA 1979 SLO 0:16:10 0:32:20'))

def naj_pospesek(vrstice):
    