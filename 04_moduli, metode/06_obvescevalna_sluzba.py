msg = """Dragi Ahmed,

kako si kaj? Upam, da so otroci ze zdravi.

Mustafa, Osama in jaz smo se sli danes malo razgledat in
kaze kar dobro. Abdulah pa ni mogel zraven, je sel v Pesavar
prodat se tri kamele. Osama sicer pravi, da se mu to pred
zimo ne splaca, ampak saj ves, kaksen je Abdulah. Harun in
on, nic jima ne dopoves, se Osama ne. Jibril me klice,
moram iti; oglasi se kaj na Skype!

tvoj Husein

PS, oprosti za sumnike - rashmeD nas je preprical, da zdaj
uporabljamo Python.
"""

import re

msg = re.sub("[^\w ]", " ", msg)

print(msg)

imena = []
ponovitev = []

besede = msg.split()
for beseda in besede:
    if beseda[0].isupper():
        if beseda not in imena:
            imena.append(beseda)
            ponovitev.append(1)
        else:
            for zap, ime in enumerate(imena):
                if ime == beseda:
                    ponovitev[zap] += 1

for x, y in zip(imena, ponovitev):
    print(x, ' ', y, '  ')