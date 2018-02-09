import tester

tests = [
    ('Test na manjših številih', [
        (1, True), 
        (2, False),
        (7, False),
        (25, True),
        (27, False),
        (1234, False),
        (9876, False),
        (123**2, True),
        (123**2 + 1, False),
    ]),

    ('Test na velikih številih (težje)', [
        (123456789**2, True),
        (123456789**2 + 1, False),
        (123456789**2 - 1, False),
        (5613524678954351234687**2, True),
        (5613524678954351234687**2 + 1, False),
        (5613524678954351234687**2 - 1, False),
    ]),
]

for msg, inputs in tests:
    print(msg + '\n' + '-' * len(msg))
    in_out = []
    for n, isprime in inputs:
        in_out.append(((n,), 'Vpiši število: Število {} kvadrat\n'.format('je' if isprime else 'ni')))
    tester.check('kvadrati.py', in_out)
    print()
