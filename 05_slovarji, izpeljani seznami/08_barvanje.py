import collections

barve = [("A3", "zelena"), ("B5", "modra"), ("A3", "rumena")]

def barvanje(barve):
    sahovnica = collections.defaultdict()
    for polje, barva in barve:
        if polje in sahovnica:
            continue
        sahovnica[polje] = barva
    return sahovnica

print(barvanje(barve))

######################################################################

sahovnica = {
    "A3": "rumena", "A6": "rumena", "H2": "rumena", "G7": "rumena",
    "C2": "zelena", "C3": "zelena",
    "H6": "modra"
}

def prestej_barvo(sahovnica, barva):
    ponovitev = 0
    for barva1 in sahovnica.values():
        if barva1 == barva:
            ponovitev += 1
    return ponovitev

print(prestej_barvo(sahovnica, 'rumena'))