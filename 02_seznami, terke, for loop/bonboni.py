zaporedje = [4, 0, 2, 3, 2, 0, 3, 4, 4, 4]

ima_bonbon = [0] * 6
for otrok in zaporedje:
    ima_bonbon[otrok] += 1
for ima in ima_bonbon:
    if not ima:
        print('Ne')
        break