
vredt = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]

def kronogram(s):
    v = 0
    for znak, stev in vredt:
        v += s.count(znak) * stev
    return v

i = input('vpiši kronogram')

print(kronogram(i))