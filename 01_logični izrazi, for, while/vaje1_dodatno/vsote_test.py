import tester

tests = [
    ('Test na manjših številih', 
        [(1, 1), 
         (2, 3), 
         (7, 28), 
         (100, 5050),
         (1000, 500500),
         (45367, 1029105028),
        ]),
    ('Test na velikih številih (težje)', 
        [(123456, 7620753696), 
         (123456789, 7620789436823655),
         (123456789987654321, 7620789497027892162094192888812681),
         (134958734958279867346923409818, 
          9106930070769616173978874265286493359236600279547451101471),
        ]),
]

for msg, inputs in tests:
    print(msg + '\n' + '-' * len(msg))
    in_out = []
    for n, m in inputs:
        in_out.append(((n,), 'Vpiši število: {}\n'.format(m)))
    tester.check('vsote.py', in_out)
    print()
