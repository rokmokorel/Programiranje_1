import math

def prastevila(n):
    cnt = 0
    for i in range (2, n):
        for j in range(2, int(math.sqrt(i)+1)):
            if i % j == 0:
                break
        else:
            cnt += 1
    return cnt

print(prastevila(10))