from functools import reduce
import operator


def check_3cnf(phi):
    numbers = []
    disjuncts = phi.split("and")
    for i in range(len(disjuncts)):
        disjuncts[i] = disjuncts[i].split("or")
        if (len(disjuncts[i]) != 3):
            return (False, "invalid number of literals in disjunct %s" %
                           disjuncts[i])
        for j in range(3):
            disjuncts[i][j] = disjuncts[i][j].split("not")
            if not (1 <= len(disjuncts[i][j]) <= 2):
                return (False, "invalid literal %s" % str(disjuncts[i][j]))
            try:
                disjuncts[i][j][-1] = int(disjuncts[i][j][-1])
                numbers += [disjuncts[i][j][-1]]
            except ValueError:
                return (False, "invalid literal %s" % disjuncts[i][j])
    numbers = sorted(list(set(numbers)))
    if (numbers != list(range(len(numbers)))):
        return (False, "invalid variables names")
    return (True, disjuncts, len(numbers))


def run_3cnf(disjuncts, est):
    for i in range(len(disjuncts)):
        for j in range(3):
            disjuncts[i][j][-1] = est[disjuncts[i][j][-1]]
            if (len(disjuncts[i][j]) > 1):
                disjuncts[i][j][-1] = not disjuncts[i][j][-1]
            disjuncts[i][j] = disjuncts[i][j][-1]
        disjuncts[i] = reduce(operator.__or__, disjuncts[i])
    return reduce(operator.__and__, disjuncts)
