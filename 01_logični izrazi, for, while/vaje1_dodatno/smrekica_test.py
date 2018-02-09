import tester

in_out = [
    [(1,), '*\n'],
    [(2,), ' *\n***\n'],
    [(3,), '  *\n ***\n*****\n'],
    [(4,), '   *\n  ***\n *****\n*******\n'],
    [(6,), '     *\n    ***\n   *****\n  *******\n *********\n***********\n'],
]

for xs in in_out:
    xs[1] = 'Vpiši višino: ' + xs[1]
tester.check('smrekica.py', in_out)
