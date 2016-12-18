from cnf_utils import run_3cnf, check_3cnf


def get_value(literal, variable):
    return (len(literal) == 2) != variable


def unit_propagate(phi, rho):
    flag = True
    while flag:
        flag = False
        for disjunct in phi:
            a, b, c = [disjunct[i][-1] for i in range(3)]
            if ((a in rho) + (b in rho) + (c in rho) >= 2):
                second_flag = False
                for i in range(3):
                    second_flag |= (disjunct[i][-1] in rho and
                                    get_value(disjunct[i],
                                              rho[disjunct[i][-1]]))
                if ((a in rho) + (b in rho) + (c in rho) == 3 and
                   not second_flag):
                    return False
                for i in range(3):
                    if not disjunct[i][-1] in rho:
                        if not second_flag:
                            rho[disjunct[i][-1]] = (len(disjunct[i]) == 1)
                phi.remove(disjunct)
                flag = True
                break
    return True


def dpll(phi, rho, n):
    if (not unit_propagate(phi, rho)):
        return False
    if (len(rho) == n):
        est = [int(rho[i]) if i in rho else 0 for i in range(n)]
        new_phi = [list(i) for i in phi]
        for i in new_phi:
            for j in range(len(i)):
                i[j] = list(i[j])
        if run_3cnf(new_phi, est):
            return (True, est)
        return False
    for i in range(n):
        if (i not in rho):
            rho[i] = True
            result = dpll(phi, rho, n)
            if (result):
                return result
            pho[i] = False
            return dpll(phi, rho, n)


def check_3sat(phi):
    phi, n = check_3cnf(phi)[1:]
    old_rho = {}
    for i in phi:
        for j in i:
            old_rho[(j[-1], len(j))] = True
    rho = {}
    for i in range(n):
        if (i, 1) not in old_rho:
            rho[i] = False
        elif (i, 2) not in old_rho:
            rho[i] = True
    for i in phi:
        for j in range(len(i)):
            i[j] = tuple(i[j])
    phi = set([tuple(i) for i in phi])

    flag = False
    to_remove = []
    for i in phi:
        for j in i:
            if (j[-1] in rho):
                flag = True
        if (flag):
            to_remove += [i]
            flag = False
    for i in to_remove:
        phi.remove(i)
    if (len(phi) == 0):
        return (True, [int(rho[i]) if i in rho else 0 for i in range(n)])
    return dpll(phi, rho, n)
