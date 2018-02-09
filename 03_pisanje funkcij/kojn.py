def polje_v_koord(polje):
    return ord(polje[0]) - 64, int(polje[1])


def koord_v_polje(x, y):
    return chr(x + 64) + str(y)


def legalne_koord(a, b):
    return 0 < a <= 8 and 0 < b <= 8


print(legalne_koord(0,4))


# ********************************* REŠEVANJE ZA 6 *********************************

def moznosti(polje):
    x, y = polje_v_koord(polje)
    return [koord_v_polje(x+dx, y+dy)
        for dx, dy in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        if legalne_koord(x+dx, y+dy)]

print(moznosti('A4'))

# ********************************* REŠEVANJE ZA 7 *********************************

def legalna(polje1, polje2):
    return polje2 in moznosti(polje1)
print(legalna('A4', 'B4'))

# ********************************* REŠEVANJE ZA 8 *********************************

def legalna_pot(pot):
    return all(legalna(polje1, polje2) for polje1, polje2 in zip(pot, pot[1:]))

print('za osem: ', legalna_pot(["F3", "E1", "G3", "H5"]))

# ********************************* REŠEVANJE ZA 9 *********************************

def obhod(pot):
    return len(pot) == 65 and len(set(pot)) == 64 and pot[0] == pot[-1] and legalna_pot(pot)

print(obhod(["A2", "B4", "D3"]))

# ********************************* REŠEVANJE ZA 10 *********************************

def razdalje():
    sahovnica = []
    for i in range(8):
        sahovnica.append([-1] * 8)
    sahovnica[0][0] = 0
    obiskanih = 1
    skok = 1
    while obiskanih < 64:
        for x in range(1,8):
            for y in range(1,8):
                if sahovnica[x-1][y-1] == skok-1:
                    for kam in moznosti(koord_v_polje(x,y)):
                        xn, yn = polje_v_koord(kam)
                        if sahovnica[xn-1][yn-1] < 0:
                            sahovnica[xn-1][yn-1] = skok
                            obiskanih += 1
        skok += 1
    s = ""
    for vrstica in sahovnica:
        for skokov in vrstica:
            s += str(skokov)
        s += "\n"
    return s
print(razdalje())

# ------------- hitrejša --------------
def razdalje_hitro():
    sahovnica = [[-1] * 8 for i in range(8)]
    sahovnica[0][0] = 0
    kandidati = ["A8"]
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
print(razdalje_hitro())