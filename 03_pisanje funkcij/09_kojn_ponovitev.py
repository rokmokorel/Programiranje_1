def polje_v_koord(polje):
    return ord(polje[0]) - 64, int(polje[1])

def koord_v_polje(x, y):
    return chr(x + 64) + str(y)

def legalne_koord(x, y):
    return 0 < x < 9 and 0 < y < 9
print(legalne_koord(1,5))

# ************************ OCENA 6 ************************
def moznosti(polje):
    x, y = polje_v_koord(polje)
    return [koord_v_polje(x+dx, y+dy)
            for dx, dy in
            ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
            if legalne_koord(x+dx, y+dy)]
print(moznosti("B4"))

# ************************ OCENA 7 ************************
def legalna(polje1, polje2):
    return polje2 in moznosti(polje1)
print(legalna("A1", "B3"))

# ************************ OCENA 8 ************************
def legalna_pot(pot):
    for i in range(len(pot)-1):
        if not pot[i+1] in moznosti(pot[i]):
            return False
    return True
print(legalna_pot(["F3", "E1", "G3", "H5"]))

# ************************ OCENA 9 ************************
def obhod(pot):
    if len(pot) != 65 or pot[0] != pot[-1] or not legalna_pot(pot):
        return False
    for i, polje in enumerate(pot):
        if polje in pot[:i]:
            return False
    return True
print(obhod(["A2", "B4", "D3"]))

# ************************ OCENA 10 ************************
def razdalje():
    sahovnica = [[-1] * 8 for i in range(8)]
    sahovnica[0][0] = 0
    kandidati = ['A8']
    while kandidati:
        polje = kandidati.pop(0)
        x, y = polje_v_koord(polje)
        skokov = sahovnica[x-1][8-y]
        for naprej in moznosti(polje):
            x, y = polje_v_koord(naprej)
            if sahovnica[x-1][8-y] == -1:
                sahovnica[x-1][8-y] = skokov+1
                kandidati.append(naprej)

    s = ""
    for vrstica in sahovnica:
        for skokov in vrstica:
            s += str(skokov)
        s += "\n"
    return s
print(razdalje())