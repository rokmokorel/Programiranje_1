stavek = "Tole je primer     za domaco nalogo"
besede = []
zad_pres = -1
i = 0

for i in range(len(stavek)+1):
    if i == len(stavek) or stavek[i] == " ":
        if i != zad_pres + 1:
            besede.append(stavek[zad_pres+1:i])
        zad_pres = i
    i += 1
print(besede)