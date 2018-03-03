def collatz(n):
    s = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        s.append(n)
    return s
print(collatz(8))

def collatz_dolzina(n):
    return len(collatz(n))
print(collatz_dolzina(8))

def najdaljsi_dolz(n):
    naj = naj_t = 0
    for i in range(1, n+1):
        t = collatz_dolzina(i)
        if t > naj:
            naj, naj_t = t, i
    return naj_t
print(najdaljsi_dolz(10000))

def nad_n(s):
    i = 1
    while True:
        if collatz_dolzina(i) >= s:
            return i
        i += 1
print(nad_n(10))


