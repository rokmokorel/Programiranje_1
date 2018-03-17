rodbina = {
    "Adam": ["Matjaž", "Cilka", "Daniel"],
    "Aleksander": [],
    "Alenka": [],
    "Barbara": [],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Erik": [],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
    "Franc": [],
    "Herman": ["Margareta"],
    "Hans": ["Herman", "Erik"],
    "Jožef": ["Alenka", "Aleksander", "Petra"],
    "Jurij": ["Franc", "Jožef"],
    "Ludvik": [],
    "Margareta": [],
    "Matjaž": ["Viljem"],
    "Petra": [],
    "Tadeja": [],
    "Viljem": ["Tadeja"],
}

starost = {
    "Adam": 111, "Matjaž": 90, "Cilka": 88, "Daniel": 85, "Erik": 83,
    "Viljem": 58, "Tadeja": 20, "Elizabeta": 68, "Hans": 64, "Ludvik": 50,
    "Jurij": 49, "Barbara": 45, "Herman": 39, "Mihael": 32, "Franc": 30,
    "Jožef": 29, "Margareta": 3, "Alenka": 9, "Aleksander": 5, "Petra": 7}


def stevilo_otrok(oseba):
    return len(rodbina[oseba])


print(stevilo_otrok('Adam'))


def stevilo_vnukov(oseba):
    v = 0
    for otrok in rodbina[oseba]:
        v += len(rodbina[otrok])
    return v


def stevilo_vnukov_2(oseba):
    return sum(stevilo_otrok(otrok) for otrok in rodbina[oseba])


print(stevilo_vnukov('Adam'))
print(stevilo_vnukov_2('Adam'))


def velikost_rodbine(oseba):
    v = 0
    for otrok in rodbina[oseba]:
        v += velikost_rodbine(otrok)
    return v + 1

def velikost_rodbine2(oseba):
    return sum(velikost_rodbine(otrok) for otrok in rodbina[oseba]) + 1

print(velikost_rodbine('Adam'))
print(velikost_rodbine2('Adam'))


def obstaja_ime(oseba, ime):
    if oseba == ime:
        return True
    for otrok in rodbina[oseba]:
        if obstaja_ime(otrok, ime):
            return True
    return False

def obstaja_ime2(oseba, ime):
    return oseba == ime or any(obstaja_ime(otrok, ime) for otrok in rodbina[oseba])

print(obstaja_ime('Adam', 'Cilka'))
print(obstaja_ime2('Adam', 'Cilka'))

def najvec_otrok(oseba):
    naj = len(rodbina[oseba])
    for otrok in rodbina[oseba]:
        koliko = najvec_otrok(otrok)
        if  koliko > naj:
            naj = koliko
    return naj

def najvec_otrok2(oseba):
    return max([len(rodbina[oseba])] + [najvec_otrok2(otrok) for otrok in rodbina[oseba]])

print(najvec_otrok('Cilka'))

def globina_rodbine(oseba):
    globina = 0
    for otrok in rodbina[oseba]:
        g = globina_rodbine(otrok)
        if g > globina:
            globina = g
    return globina + 1
print(globina_rodbine('Adam'))