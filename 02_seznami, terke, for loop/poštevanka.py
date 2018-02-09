for i in range(1,101):
    if i % 10 == 7 or i // 10 == 7:
        print('BUM', end='  ')
    else:
        print(i, end=' ')