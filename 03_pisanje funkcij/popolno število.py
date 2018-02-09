def popolno_stevilo(i):
    pop_stevilo = []
    for stevilo in range(i):
        deljitelji = []
        for deljitelj in range(1,stevilo):
            if stevilo % deljitelj == 0:
                deljitelji.append(deljitelj)
        if sum(deljitelji) == stevilo:
            pop_stevilo.append(stevilo)
    return pop_stevilo

print(popolno_stevilo(1000))