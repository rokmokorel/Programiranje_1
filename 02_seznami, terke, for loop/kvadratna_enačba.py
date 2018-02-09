import math

a = int(input('Vpiši a: '))
b = int(input('Vpiši b: '))
c = int(input('Vpiši c: '))

d = b**2 - 4 * a * c

if d < 0:
    print('Enačba nima realnih rešitev')
elif d == 0:
    x = -b / (2 * a)
    print('enačba ima eno realno rešitev', x)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('enačba ima dve rešitvi: ', x1,'in', x2)