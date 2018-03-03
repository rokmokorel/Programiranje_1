seznam = ['ele1', 'ele2', 'ele3', 'ele1']

def ostevilci(xs):
    xs_novi = []
    for i in range(len(seznam)):
        xs_novi.append((i, seznam[i]))
    return xs_novi

def ostevilci2(xs):
    return list(enumerate(xs))

print(ostevilci(seznam))
print(ostevilci2(seznam))