import tester

tests = [
    ('Test na manjših številih', [
        (0, 0, 0),
        (1, 1, 0),
        (2, 2, 2),
        (3, 2, 1),
        (4, 2, 0),
        (5, 3, 4),
        (20, 5, 5),
        (120, 11, 1),
        (121, 11, 0),
        (122, 12, 22),
        (1234**2, 1234, 0),
        (1234**2 + 1, 1235, 2468),
    ]),

    ('Test na velikih številih (težje)', [
        (123456789**2, 123456789, 0),
        (123456789**2 + 1, 123456790, 246913578),
        (123456789987654321**2, 123456789987654321, 0),
        (123456789987654321**2 + 1, 123456789987654322, 246913579975308642),
    ]),
]

for msg, inputs in tests:
    print(msg + '\n' + '-' * len(msg))
    in_out = []
    for n, m, o in inputs:
        in_out.append(((n,), 
            'Vpiši število kock: Potrebujemo škatlo širine {} v kateri je '
            'prostora še za {} kock\n'.format(m, o)))
    tester.check('kocke_z_luknjo.py', in_out)
    print()
