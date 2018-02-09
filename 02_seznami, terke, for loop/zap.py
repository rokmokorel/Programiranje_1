
zenske = [158, 166, 150, 158, 152, 160, 172, 159, 158, 162]
moski =  [168, 172, 181, 166, 172, 174, 165, 169, 169, 185]


def najm_razlika(zenske, moski):
    return max(abs(e1 - e2) for e1, e2 in zip(zenske, moski))

najm_najv_raz, najm_odm = min((najm_razlika(zenske, moski[odm:] + moski[:odm]), odm) for odm in range(len(moski)))

print(najm_najv_raz, najm_odm)
print(najm_razlika(sorted(zenske), sorted(moski)))