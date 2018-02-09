zenske = [158, 166, 150, 158, 152, 160, 172, 159, 158, 162]
moski = [168, 172, 181, 166, 172, 174, 165, 169, 169, 185]


najm_raz = 1000
for odm in range(len(moski)):
    naj_raz = 0
    for e1, e2 in zip(zenske, moski[odm:] + moski[:odm]):
        if abs(e1 - e2) > naj_raz:
            naj_raz = abs(e1 - e2)
    if naj_raz < najm_raz:
        najm_raz = naj_raz
        naj_odm = odm
print(naj_odm, najm_raz)