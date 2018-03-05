def poisci_stevilko(s):
    for beseda in s.split():
        if beseda.isnumeric():
            return int(beseda)
print(poisci_stevilko('to Ne 001'))

#----------------------------------------------------------------------

niz = '''Štejmo kot ljudje in tej vrstici recimo prva, naprej pa v 4
V drugi vrstici sta številki 10 in 8.
Tretja vrstica nima nobene številke. 
Ta je četrta in v vrstici 12 se reč nadaljuje 
V peti vrstici še nismo končali, saj v vrsti 8 nadaljujemo. 
V šesti je 6 in to je lahko zoprno. A ne bo. 
Sedma je zoprna, saj poleg številke 5 vsebuje tudi 18 za zafrkavanje 
Osma vrstica je zadnja, tu končamo. 
Te tri vrstice so pa dolgočasne. 
Prav res. 
V enajsti vidimo, da je šele vrstica 12 je spet zanimiva 
Ta je zadnja, dvanajsta, ampak zdaj gremo v vrsto 7

'''

def poisci_zadnjo(s):
    vrstice = s.split('\n')
    kje = 1
    while kje:
        trenutna = vrstice[kje - 1]
        kje = poisci_stevilko(trenutna)
    return trenutna

print(poisci_zadnjo(niz))



