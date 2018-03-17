for vrstica in open('podatki.txt', encoding='utf-8'):
    print(vrstica.strip())

seznam = []
for vrstica in open('podatki.txt', encoding='utf-8'):
    mesto, vreme, temp = vrstica.strip().split(';')
    seznam.append((mesto, vreme, float(temp)))
print(seznam)

seznam = []
print('{:15}{:^15}{:15}'.format('Kraj', 'Vreme', 'Temperatura(˚F)'))
print('-' * 45)
for vrstica in open('podatki.txt', encoding='utf-8'):
    mesto, vreme, temp = vrstica.strip().split(';')
    print('{mesto:.<15}{vreme:.^15}{temp:.>15}'.format(**locals()))

out = open('vreme.txt', 'w', encoding='utf-8')
out.write('{:15}{:^15}{:15}'.format('Kraj', 'Vreme', 'Temperatura(˚F)\n'))
out.write('-' * 45)
for vrstica in open('podatki.txt', encoding='utf-8'):
    out.write('\n{mesto:.<15}{vreme:.^15}{temp:.>15}'.format(**locals()))

