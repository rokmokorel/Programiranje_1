import tester

in_out = [("beseda", False), ("vsedel", True), ("parmezan", True), ("uspelo", False)]

in_out = [
    (i, "Vnesi besedo: %s\n" % ((i + " najbrž ni pravilna slovenska beseda")*f))
    for i, f in in_out]

tester.check("naloga_a.py", in_out)
