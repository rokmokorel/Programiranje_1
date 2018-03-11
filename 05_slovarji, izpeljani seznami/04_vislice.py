def getCharPos(word, char):
    ret = []
    for i in range(len(word)):
        if word[i] == char:
            ret.append(i)
    return ret
print(getCharPos("PONUDNIK","N"))

############################################################

def haveAllChars(word, chars):
    for crka in word:
        if crka not in chars:
            return False
    return True
print(haveAllChars("AMFITEATER", {"A", "M"}))

############################################################

def showChars(word, chars):
    zlozenka = ''
    for crka in word:
        if crka not in chars:
            zlozenka += '.'
        else:
            zlozenka += crka
    return zlozenka
print(showChars("PONUDNIK", set()))

############################################################
import os
from unipath import Path

for i in range(3):
    os.chdir('..')
p = Path(os.getcwd() + '/downloads/programiranje/samostalniki.txt')

os.fopen(p)
print(p.ext)
