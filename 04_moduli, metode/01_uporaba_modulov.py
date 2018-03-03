# modul math
import math

print('{:.2f}, {:.2f}'.format(math.pi, math.log(2,10)))

# modul random
import random
print('{}, {:.2f}'.format(random.randint(1,4), random.gauss(30.1, 1.2)))

# modul os, delo z datotekami
import os
for i in range(4):
    os.chdir('..')

os.chdir('rok/Downloads')

for fname in os.listdir('.'):
    if fname == 'gendatoteka.txt':
        os.rename(fname, 'gen2dat.txt')

