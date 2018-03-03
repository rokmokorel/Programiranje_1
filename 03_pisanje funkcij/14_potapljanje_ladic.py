def prazna(n):
    return [''] * n

#-----------------------------------------------------------------------------

def je_prazna(plosca):
    for i in plosca:
        if i == '':
            return False
    return True

#-----------------------------------------------------------------------------

def v_niz(plosca):
    ret =  ''
    for _ in plosca:
        if _ == '':
            ret += ' '
        else:
            ret += _
    return ret

def v_niz_1(plosca):
    return ''.join(c or ' ' for c in plosca)

print(v_niz(['', 'a', '', '', '', 'x', 'x', 'x', '', 'y', 'y', '', '']))

#-----------------------------------------------------------------------------

niz = ['', 'a', '', '', '', 'x', 'x', 'x', '', 'y', 'y', '', '']
def je_prostor(plosca, kje, dolzina):
    return dolzina <= len(plosca) and \
    je_prazna(plosca[kje:kje + dolzina]) and \
    (kje == 0 or plosca[kje-1] == '') and \
    (kje + dolzina >= len(plosca) or plosca[kje + dolzina] == '')
print(je_prostor(niz, 0,2))

#-----------------------------------------------------------------------------

def postavi(plosca, kje, dolzina, oznaka):
    if je_prostor(plosca, kje, dolzina):
        plosca[kje:kje+dolzina] = oznaka * dolzina
        return True
    return False

print(postavi(niz, 2,3, 'd'))
print(niz)

#-----------------------------------------------------------------------------

def obstaja(plosca, oznaka):
    return oznaka in plosca
print(obstaja(niz, 'a'))

#-----------------------------------------------------------------------------

def vse_oznake(plosca):
    ret = []
    for i in plosca:
        if i and i not in ret:
            ret.append(i)
    return ret
print(vse_oznake(niz))

def vse_oznake_1(plosca):
    return list(set(plosca))

#-----------------------------------------------------------------------------

def strel(plosca, kje):
    oznaka = plosca[kje]
    if oznaka == '':
        return 0
    plosca[kje] = ''
    if obstaja(plosca, oznaka):
        return 1
    elif je_prazna(plosca):
        return 3
    else:
        return 2

print(strel(niz, 5))

#-----------------------------------------------------------------------------

def razpostavi(n, ladje):
    plosca = [' ']
    for oz, dol in ladje:
        plosca += [oz] * dol
        plosca.append('')
    del plosca[-1]
    plosca += [''] * (n-len(plosca))
    return plosca

print(razpostavi(12, [('a', 2), ('b', 3), ('c', 1)]))