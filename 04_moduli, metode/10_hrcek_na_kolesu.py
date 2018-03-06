def v_seznam(s):
    casi = []
    podatki = s.split(';')
    for i in podatki:
        i = i.replace(',', '.')
        casi.append(float(i))
    return casi


print(v_seznam("5,180; 5,907; 6,632; 7,215"))

##################################################

def v_niz(s):
    casi = []
    for i in s:
        i = str(i)
        i = i.replace('.', ',')
        casi.append(i)
    return '; '.join(casi)


print(v_niz([5.18, 5.907, 6.632, 7.215]))

##################################################

def oznaci_veljavne(casi):
    meritve = [True] * len(casi)
    for i in range(len(casi) - 1):
        if casi[i + 1] - casi[i] < 0.1:
            meritve[i + 1] = meritve[i] = False
    return meritve


print(oznaci_veljavne([5.1, 5.6, 6.0, 10.34, 10.37, 10.45, 12.5]))

##################################################

def veljavne(casi):
    meritve = []
    veljavne = oznaci_veljavne(casi)
    for vel, cas in zip(veljavne, casi):
        if vel:
            meritve.append(cas)
    return meritve


print(veljavne([5.1, 5.6, 6.0, 10.34, 10.37, 10.45, 12.5]))


def veljavne_boljsa(casi):
    return [x for x, y in zip(casi, oznaci_veljavne(casi)) if y]


print(veljavne([5.1, 5.6, 6.0, 10.34, 10.37, 10.45, 12.5]))

##################################################

def brez_napacnih_casov(casi):
    pravilni = []
    prej = -1
    for cas in casi:
        if cas > prej:
            pravilni.append(cas)
            prej = cas
    return pravilni


print(brez_napacnih_casov([5.1, 5.6, 6.0, 10.34, 10.37, 10.45, 12.5]))
