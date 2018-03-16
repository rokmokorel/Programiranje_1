from math import *

k = [sqrt(x) for x in [9, 16, 81, 25, 196]]
print(k)

# izračunamo povprečno dolžino imena

imena = ["Ana", "Berta", "Cilka", "Dani", "Ema"]

print(sum([len(ime) for ime in imena]) / len(imena))

# izračunamo povprečno težo

podatki = [
    (74, "Anže", False),
    (82, "Benjamin", False),
    (58, "Cilka", True),
    (66, "Dani", False),
    (61, "Eva", True),
    (84, "Franc", False),
]

vsota = sum([teza for teza, ime, spol in podatki])
print(vsota/len(podatki))

# seznam sodih števil

s = [x for x in range(100) if (x % 2 == 1) and ('2' not in str(x))]
print(s)



