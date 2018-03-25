def palidrom(s):
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True

print(palidrom('SoS'))

def palindrom2(s):
    return len(s) < 2 or s[0] == s[-1] and palidrom(s[1:-1])

print(palindrom2('abradakadarba'))

def vsota_seznama(s):
    if not s:
        return 0
    return s[0] + vsota_seznama(s[1:])

print(vsota_seznama([2,00,10]))

def soda(s):
    if not s:
        return True
    return soda(s[1:]) and s[0] % 2 == 0

def soda2(s):
    return not s or soda2(s[1:]) and s[0] % 2 == 0

print(soda([2, 12, 5]))
print(soda2([2, 12, 4]))

