# -*- coding: utf-8 -*-

import tester

in_out = [
    ("Stavek, ki vsebuje takšne in drugačne besede. Netakere so pravilne, druhe ne.",
         ['netakere', 'druhe']),
    ("Tegale pa je napisal skoraj pravi Top o riši", []),
    ("Kocka je padla, Rubikon je pretacan. Ah, ta Rubikon!", ["rubikon", "pretacan"]),
    ("", []),
    ("Valjhun, sin Kajtimara, boj krvavi že dolgo bije za krščansko vero",
         ['valjhun', 'kajtimara'])]

in_out = [(i, "Vnesi stavek: %s\n" % o) for i, o in in_out]

tester.check("naloga_b.py", in_out)
