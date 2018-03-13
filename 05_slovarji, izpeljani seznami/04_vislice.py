def getCharPos(word, char):
    ret = []
    for i in range(len(word)):
        if word[i] == char:
            ret.append(i)
    return ret


print(getCharPos("PONUDNIK", "N"))


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
# import os
import random

datoteka = open('samostalniki.txt', mode='r')


def vislice():
    besede = datoteka.read().splitlines()
    print(besede)
    beseda = random.choice(besede).strip("'")
    print(beseda)
    zivljenj = 6
    izbrane = set()
    while zivljenj:
        print(showChars(beseda, izbrane), zivljenj)
        ugib = input('Ugani črko: ')
        izbrane.add(ugib.lower())
        izbrane.add(ugib.upper())
        print(showChars(beseda, izbrane))
        if haveAllChars(beseda, izbrane):
            print('Bravo')
            break
        if not ugib.lower() or ugib.upper() in beseda:
            print(beseda)
            print(type(beseda))
            zivljenj -= 1
        print('\n')
    if not zivljenj:
        print('Konec igre, iskana beseda je {}'.format(beseda))


vislice()
