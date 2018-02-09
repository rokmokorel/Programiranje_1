# -*- coding: utf-8 -*-

import tester

besede = ["brcatig", "besedr", "hg"]

in_out = [("\n".join(beseda),
           "".join("Tekmovalec %i, črka? " % (i % 2 + 1) for i in range(len(beseda)))
           + "Nobena beseda se ne začne z " + beseda
          ) for beseda in besede]

tester.check("naloga_c.py", in_out)
