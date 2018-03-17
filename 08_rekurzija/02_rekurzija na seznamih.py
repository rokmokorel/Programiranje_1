def palidrom(s):
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True

print(palidrom('SoS'))

def palidrom2(s):
