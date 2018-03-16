# vsota kvadratov naravnih števil
print(sum(x**2 for x in range(101)))

# vsota polindromnih števil
print(sum(x**2 for x in range(1000) if str(x) == str(x)[::-1]))

# premeči črke
def subs(niz, polozaj):
    return ''.join(niz[int(i)] for i in polozaj)
print(subs("abc", "0002"))

# povprečje, standardni odklon
xs = [183, 168, 175, 176, 192, 180]
def mean(niz):
    return sum(x for x in niz) / len(niz)
print(mean(xs))

from math import sqrt
def std(niz):
    return sqrt(1/len(niz) * sum((x - mean(niz))**2 for x in niz) )
print(std(xs))

# morsejeva abeceda
morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': ''
}
def txt2morse(niz):
    return ''.join(morse[c] for c in niz)

# ISBN
def valid(niz):
    return sum(int(niz[c-1]) * c for c in range(1,11)) % 11 == 0 and len(niz) == 10
print(valid('0306406152'))
