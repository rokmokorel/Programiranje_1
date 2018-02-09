import tester

in_out = [
    [(1,), '1\n'],
    [(3,), '1\n3\n'],
    [(18,), '1\n2\n3\n6\n9\n18\n'],
    [(42,), '1\n2\n3\n6\n7\n14\n21\n42\n'],
    [(120,), '1\n2\n3\n4\n5\n6\n8\n10\n12\n15\n20\n24\n30\n40\n60\n120\n'],
    [(121,), '1\n11\n121\n'],
    [(122,), '1\n2\n61\n122\n'],
    [(12345,), '1\n3\n5\n15\n823\n2469\n4115\n12345\n'],
]

for xs in in_out:
    xs[1] = 'Vpiši število: ' + xs[1]
tester.check('delitelji.py', in_out)
