from random import *
import numpy as np

while True:
    oddaljenost_tarce = randint(0, 100) / 10

    print(oddaljenost_tarce)
    hitrost = float(input('Vnesite začetno hitrost izstrelka: '))
    kot_S = float(input('Vnesite kot strela v stopinjah: '))

    kot_R = kot_S * np.pi / 360

    dolzina_leta = hitrost ** 2 / (2 * 9.81) * np.sin(2 * kot_R)

    odstopek = oddaljenost_tarce - dolzina_leta

    if oddaljenost_tarce - 0.8 <= dolzina_leta <= float(oddaljenost_tarce) + 0.8:
        print('Ćestitke, zadeli ste tarčo')
        break

    else:
        print('Žal ste tarčo zgrešili, poskusite ponovno')
        print('Tarčo ste zgrašili za {:.2}'.format(odstopek))
