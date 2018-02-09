stevilo = int(input('Vpiši število: '))
vsota = 0
for i in range(1, stevilo):
    if stevilo % i == 0:
        vsota += i

if vsota == stevilo:
    print('število je popolno število')
else:
    print('število ni popolno število')