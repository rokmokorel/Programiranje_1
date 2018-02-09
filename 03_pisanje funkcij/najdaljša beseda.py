def najdaljsa(niz):
    naj_bes = ''
    for i in niz.split(' '):
        if len(i) > len(naj_bes):
            naj_bes = i

    return naj_bes

print(najdaljsa('an ban pet podgan'))