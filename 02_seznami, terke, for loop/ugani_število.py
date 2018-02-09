from random import randint

od = int(input('Spodnja meja območja: '))
do = int(input('Zgornja meja območja: '))

binarno = ''
odziv = ''
poskus = 0
while poskus <= 10 and odziv != 'bravo':
    poskus += 1
    ugib = randint(od, do)
    odziv = input('Ali je to število {}? '.format(ugib))
    if odziv == 'več':
        od = ugib + 1
        binarno += '1'
    elif odziv == 'manj':
        do = ugib - 1
        binarno += '0'
    elif odziv == 'bravo':
        print('Potreboval sem {} poskusov'.format(poskus))
        print(binarno)
        break
    else:
        print('vstavite manj/več/bravo')