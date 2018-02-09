besede_sskj = open("00_mte-sl.words.txt", encoding="latin2").read().lower().split()
beseda = ""
tekmovalec = 1
pravilna = True
while pravilna:
    c = input('Tekmovalec {}, vnesi črko: '. format(tekmovalec))
    beseda += c
    pravilna = False
    for b in besede_sskj:
        if b[:len(beseda)] == beseda:
            pravilna = True
            break
    tekmovalec = 3 - tekmovalec
print('Nobena beseda se ne začne z {}'.format(beseda))