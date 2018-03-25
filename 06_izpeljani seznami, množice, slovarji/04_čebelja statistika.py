def po_vrstah(vrt):
    return [sum(podseznam) for podseznam in vrt]

print(po_vrstah([[3, 5, 1], [1, 1, 1], [2, 0, 4]]))

def najboljsi(vrt):
    return [max(podseznam) for podseznam in vrt]

print(najboljsi([[3, 5, 1], [1, 1, 1], [2, 0, 4]]))

def diagonala(vrt):
    return sum(vrt[i][i] for i in range(min(len(vrt), len(vrt[0]))))

print(diagonala([[3, 5, 1], [1, 1, 1], [2, 0, 4]]))

def je_polindromen(vrt):
    return all(vrsta == vrsta[::-1] for vrsta in vrt)

def polindromne(vrt):
    return [vrsta for vrsta in vrt if vrsta == vrsta[::-1]]

print(polindromne([[3, 5, 1], [1, 1, 1], [2, 0, 4]]))