knjiga = {
     "Ana":
         ["pometanje stopnic", "jezikanje", "kuhanje kosila", "pretep z bratom", "pometanje stopnic", "kuhanje kosila"],
     "Benjamin":
         ["brisanje mize", "jezikanje", "prepisana naloga", "pretep s sestro"],
     "Cilka":
         [],
     "Dani":
         ["prepir z mamo", "kuhanje kosila", "kuhanje kosila"],
     "Eva":
         ["pretep z bratom", "nenarejena naloga"],
     "Franc":
         ["pomivanje posode", "brisanje mize", "pometanje stopnic",
          "kuhanje kosila", "kuhanje kosila", "pometanje stopnic"],
     "Greta":
         ["pometanje stopnic", "jezikanje"],
     "Helga":
         ["pometanje stopnic", "jezikanje", "kuhanje kosila", "prepir z mamo", "pometanje stopnic", "kuhanje kosila"],
 }

tockovalnik = {
    'pometanje stopnic': 3,
    'kuhanje kosila': 5,
    'pomivanje posode': 3,
    'brisanje mize': 1,
    'pretep z bratom': -3,
    'pretep s sestro': -3,
    'prepir z mamo': -5,
    'nenarejena naloga': -4,
    'prepisana naloga': -7,
    'jezikanje': -4
}

cena = {
    'sanke': 20,
    'zvezek': 5,
    'lok za violino': 30,
    'barvice': 7,
    'bomboni': 3
}

def oceni(dela):
    return sum(tockovalnik[i] for i in dela)

print(oceni(["pretep s sestro", "kuhanje kosila"]))

def povzetek_knjige(stran):
    return {otrok: oceni(knjiga[otrok]) for otrok in knjiga }

print(povzetek_knjige(knjiga))

def izberi(dela, spisek):
    '''darila = set()
vsota = oceni(dela)
for zelja in spisek:
    if cena[zelja] <= vsota:
        darila.add(zelja)
return darila'''
    return {zelja for zelja in spisek if cena[zelja] <= oceni(dela)}

print(izberi(["pometanje stopnic", "pomivanje posode", "kuhanje kosila", "pretep s sestro"],
             {"zvezek", "lok za violino", "barvice", "bomboni"}))

def strosek(dela, spisek):
    return sum(cena[darilo] for darilo in izberi(dela, spisek))

print(strosek(["pometanje stopnic", "pomivanje posode", "kuhanje kosila", "pretep s sestro"],
             {"zvezek", "lok za violino", "barvice", "bomboni"}))

def najpridnejsi_otrok(otroci):
    return max((oceni(dela), ime) for ime, dela in otroci.items())[1]

print(najpridnejsi_otrok(knjiga))


def poreden(dela):
    return any(tockovalnik[delo] <= -5 for delo in dela)

print(poreden(['kuhanje kosila', 'pomivanje posode', 'prepir z mamo']))

def obdarovani(knjiga):
    return {ime for ime, dela in knjiga.items() if not poreden(dela)}

print(obdarovani(knjiga))