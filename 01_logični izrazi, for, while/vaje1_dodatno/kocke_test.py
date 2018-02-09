import tester

tests = [
    ('Test na manjših številih', [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 2),
        (4, 2),
        (5, 3),
        (20, 5),
        (120, 11),
        (121, 11),
        (122, 12),
        (1234**2, 1234),
        (1234**2 + 1, 1235),
    ]),

    ('Test na velikih številih (težje)', [
        (123456789**2, 123456789),
        (123456789**2 + 1, 123456790),
        (123456789987654321**2, 123456789987654321),
        (123456789987654321**2 + 1, 123456789987654322),
    ]),
]

for msg, inputs in tests:
    print(msg + '\n' + '-' * len(msg))
    in_out = []
    for n, m in inputs:
        in_out.append(((n,), 
            'Vpiši število kock: Potrebujemo škatlo širine {}\n'.format(m)))
    tester.check('kocke.py', in_out)
    print()
