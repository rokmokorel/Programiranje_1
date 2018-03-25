zemljevid = {0: [6, 3], 6: [5, 81], 3: [8, 24], 5: [2, 18], 81: [None, None],
             8: [42, None], 24: [63, 13], 2: [7, 27], 18: [None, 35],
             42: [None, 66], 63: [61, None], 13: [4, 12], 7: [None, None],
             27: [None, None], 35: [None, None], 66: [None, None],
             61: [None, None], 4:[None, None], 12: [None, None]}

def prehodi_pot(zeljevid, soba, pot):
    for korak in pot:
        if korak == 'L':
            soba = zeljevid[soba][0]
        else:
            soba = zemljevid[soba][1]
    return soba

print(prehodi_pot(zemljevid, 0, 'LLD'))