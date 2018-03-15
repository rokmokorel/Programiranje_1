jedi = {
    "palacinke": {"jajce": 1, "mleko": 0.3, "moka": 0.2},
    "smorn": {"jajce": 1, "mleko": 0.3, "moka": 0.2},
    "krompirjev golaz": {"krompir": 2, "paprika": 1, "cebula": 1},
    "sataras": {"paradiznik": 1, "paprika": 1, "jajce": 1, "cebula": 1, "kruh": 0.2},
    "hrenovke": {"hrenovka": 1, "kruh": 0.2},
    "makaroni": {"makaroni": 0.2, "paradiznik": 0.5, "meso": 0.2, "cebula": 0.3},
    "marmelada": {"marmelada": 0.1, "kruh": 0.3},
    "piškot": {"piškot": 2}
}


def ena_jed(jed, jedcev):
    sestavine = {}
    for sestavina, kolicina in jedi[jed].items():
        sestavine[sestavina] = kolicina * jedcev
    return sestavine


def ena_jed_boljse(jed, jedcev):
    return {sestavina: kolicina * jedcev for sestavina, kolicina in jedi[jed].items()}


print(ena_jed('palacinke', 4))
print(ena_jed_boljse('palacinke', 4))

import collections

obroki = [("makaroni", 20), ("krompirjev golaz", 25), ("hrenovke", 18),
          ("sataras", 18)]


def nakup(obroki):
    sestavine = collections.defaultdict(float)
    for jed, jedcev in obroki:
        for sestavina, kolicina in ena_jed_boljse(jed, jedcev).items():
            sestavine[sestavina] += kolicina
    return sestavine


print(nakup(obroki))

zaloga = {"jajca": 10, "mleko": 2, "moka": 2, "marmelada": 2, "kruh": 1}


def obrokov(jed, zaloga):
