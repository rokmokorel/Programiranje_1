s = ["Ana", "Berta", "Cilka", "Dani", "Ema"]

def zamenjaj(s, a, b):
    s[a], s[b] = s[b], s[a]

def preuredi(s, menjave):
    for a, b in menjave:
        zamenjaj(s, a, b)

menjave = [(2, 3), (0, 3)]
print(preuredi(s, menjave))

def urejen(s):
    if s == sorted(s):
        return True
    return False
print(urejen(s))

def urejen(s):
    for a, b in zip(s, s[1:]):
        if a > b:
            return False
    return True

def ureja(s, menjave):
    preuredi(s,menjave)
    return urejen(s)
print(ureja(s, menjave))


def nacrt(s):
    s = s[:]
    perm = []
    for i in range(len(s), 1, -1):
        for j in range(1, i):
            if s[j - 1] > s[j]:
                zamenjaj(s, j - 1, j)
                perm.append((j - 1, j))
    return perm

s = ["Ema", "Berta", "Dani", "Cilka", "Ana"]
print(nacrt(s))

