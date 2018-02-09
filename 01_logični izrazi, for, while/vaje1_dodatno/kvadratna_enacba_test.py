import tester
import math

inputs = [
    [(1, 2, 2), []],
    [(1, 2, 1), [-1.0]],
    [(1, 2, 0), [0.0, -2.0]],
    [(1, -42, 0), [42.0, 0.0]],
    [(1, 2 * -42, 42**2), [42.0]],
    [(5, 11, 4), [-0.45968757625671514, -1.7403124237432848]],
    [(5, 11, 4), [-0.45968757625671514, -1.7403124237432848]],
]

in_out = []
for input, sol in inputs:
    output = 'Vpiši a: Vpiši b: Vpiši c: '
    if len(sol) == 0:
        output += 'Enačba nima realnih rešitev.'
    elif len(sol) == 1:
        output += 'Enačba ima eno realno rešitev: {}'.format(sol[0])
    else:
        output += 'Enačba ima dve realni rešitvi: {} in {}'.format(sol[0], sol[1])
    output += '\n'
    in_out.append((input, output))

print('''OPOZORILO
Test predpostavlja, da je pri kvadratnih enačbah z dvema rešitvama
vrstni red rešitev enak kot v navodilu naloge.\n''')

tester.check('kvadratna_enacba.py', in_out)
