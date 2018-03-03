def podobnost(niz1, niz2):
    tab = ''
    cnt = 0
    for i, j in zip(niz1, niz2):
        if i == j:
           tab += '1'
           cnt += 1
        else:
            tab += '0'
    if len(niz1) != len(niz2):
        tab += '0' * abs(len(niz2) - len(niz1))
    return cnt, tab

print(podobnost('sobota', 'robot'))