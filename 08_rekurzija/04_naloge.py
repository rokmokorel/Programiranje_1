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


def izpis_imen(ime):
    print(ime)
    for otrok in rodbina[ime]:
        izpis_imen(otrok)


print(izpis_imen('Daniel'))


def imena_rodbine(ime):
    imena = [ime]
    for otrok in rodbina[ime]:
        imena.extend(imena_rodbine(otrok))
    return imena


print(imena_rodbine('Adam'))


def najmlajsi_v_rodbini(ime):
    xs = [(starost[ime], ime)]
    for otrok in rodbina[ime]:
        xs.append(najmlajsi_v_rodbini(otrok))
    return min(xs)



print(najmlajsi_v_rodbini('Adam'))


import collections
db = collections.defaultdict(list)
for line in open('trgovina.txt'):
    id, pid, name = line.strip().split(';')
    db[pid].append((id, name))

def izpis(db, pid='0', prefix=''):
    for id, name in db[pid]:
        print(prefix + name)
        izpis(db, id, prefix + name + '  /  ')

print(izpis(db))
