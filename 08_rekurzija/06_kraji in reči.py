svet = {
         "Evropa": {
             "Slovenija": {
                 "Gorenjska": {
                     "Kranj": {},
                     "Radovljica": {},
                     "Zali log": {},
                 },
                 "Štajerska": {
                     "Maribor": {},
                     "Celje": {}
                 },
                 "Osrednja": {
                     "Ljubljana": {
                         "Vič": {
                             "FRI": {
                                 "P1": {
                                     "tretja vrsta desno": {
                                         "peti stol z desne": {
                                             "Benjamin": {}
                                         }
                                     }
                                 }
                             }
                         },
                         "Šiška": {}
                     }
                 }
             },
             "Nemčija": {
                 "Bavarska": {
                     "Munchen": {}
                 },
                 "Berlin": {}
             },
         },
         "Amerika": {
             "ZDA": {
                 "Teksas": {
                     "Houston": {},
                     "Austin": {}
                 },
                 "Kalifornija": {
                     "San Francisco": {}
                 },
                 "Anchorage": {}
             },
             "Kanada": {}
         },
         "Azija": {
             "Osaka": {}
         }
        }

hisa = {
    "Klet": {
        "kurilnica": {
            "peč": {},
            "metla": {}
        },
        "shramba": {
            "spodnja polica": {
                "kisle kumare": {},
                "rdeča pesa": {}
            },
            "zgornja polica": {
                "škatla piškotov": {
                    "crknjena miš": {},
                    "pol piškota": {}
                }
            }
        },
    },
    "Prvo nadstropje": {
        "soba": {
            "računalnik": {},
            "jaz": {}
        },
        "otroška soba": {
            "Martin": {
                "ostali piškoti": {}
            }
        }
    }
}

def izpisi_vse(kraji):
    for k in kraji:
        print(k)
        izpisi_vse(kraji[k])

print(izpisi_vse(hisa))

def prestej(kraji):
    s = 0
    for k in kraji:
        s += 1 + prestej(kraji[k])
    return s

print(prestej(hisa))

def kje_je(kraj, kraji)
    for k in kraji:
        if k == kraj:
            return [k]
        pot = kje_je(kraj, kraji[k])
        if pot:
            return [k] + pot