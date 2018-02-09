i = 0
a = 0
cena = 1

while cena > 0:
    i += 1
    cena = float(input('{:<15}'.format('cena artikla:')))
    a += cena

pov = a / (i -1)

print('{:<15}'.format('Končni znesek:'), a)
print('{:<15}'.format('Povprečna cana:'), pov)
