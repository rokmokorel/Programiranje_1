locila = [',', '.']

besedilo = '''Na vratih sta se prva pojavila Ana in Peter, 
menda "slučajno". Peter se je sicer več vrtel okrog Nives. 
Kasneje sta Ana in Peter skupaj sedela na klopci, vendar je 
bil zraven tudi Benjamin. Benjamin in Ana sta skupaj pila čaj. 
Peter in Tina sta tudi pila čaj. Peter in Ana pravzaprav tisti 
večer sploh nista bila več skupaj. Nives in Peter pa. 
Ja, Nives in Peter. Tina je bila kasneje ob ribniku takrat 
kot Benjamin, le na drugi strani. Sicer pa je Tina prejšnji 
teden rekla Nives, da ima Benjamin lep čop. Benjamin definitivno 
nima lepega čopa. Tone ga ima. Ampak Tone hodi z Nives. Kura. 
Ana in Tone bi bila za skupaj. Ne pa Tone in Nives. 
'''


def poisci_imena(stavek):
    ret = []
    for beseda in stavek.split():
        if beseda.istitle():
            beseda = beseda.replace(',', '')
            ret.append(beseda)
    return ret


print(poisci_imena('Na vratih sta se prva pojavila Ana in Peter, menda "slučajno".'))


###########################################################################


def poisci_pare(besedilo):
    ret = []
    stavki = besedilo.split('.')
    for stavek in stavki:
        imena = poisci_imena(stavek)
        if len(imena) == 2:
            ret.append(sorted(imena))
        elif len(imena) == 3:
            ret.append(sorted(imena[1:]))
        else:
            continue
    return ret


print(poisci_pare(besedilo))

print(poisci_pare(besedilo))


###########################################################################

def prestej_pare(besedilo):
    pari = poisci_pare(besedilo)
    ret = []
    steto = []
    for par in pari:
        if not par in steto:
            steto.append(par)
            ret.append((pari.count(par), par))
    return ret


print(prestej_pare(besedilo))


###########################################################################

def razporedi(besedilo):
    pari = prestej_pare(besedilo)
    pari.sort(reverse=True)
    oddani = []
    koncni = []
    for pon, par in pari:
        if par[0] not in oddani and par[1] not in oddani:
            oddani += par
            koncni.append(par)
    return koncni

print('Razpored parov:')
for moski, zenska in razporedi(besedilo):
    print(moski, zenska)