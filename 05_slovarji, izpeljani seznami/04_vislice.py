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
