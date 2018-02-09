tek1 = 0
tek2 = 0

while tek1 or tek2 <= 4:
    f1 = int(input('Tekmovalec 1, prvi faktor: '))
    f2 = int(input('Trkmovalec 1: drugi faktor: '))

    pr = int(input('Tekmovalec 2, produkt: '))

    if f1 * f2 == pr:
        tek2 += 1
        print('Čestitke, {} je pravilno število'.format(tek2_produkt))

    f1 = int(input('Tekmovalec 2, prvi faktor: '))
    f2 = int(input('Tekmovalec 2, drugi faktor: '))

    pr = int(input('Tekmovalec 1, produkt'))

    if f1 * f2 == pr:
        tek1 += 1
        print('Čestitke, {} je pravilno število'.format(tek1_produkt))

    print('Trenutni rezultat: {}:{}'.format(tek1, tek2))
    print()

if tek1 > tek2:
    print('Bravo prvi')
else:
    print('Bravo drugi')