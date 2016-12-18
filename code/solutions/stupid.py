from cnf_utils import run_3cnf, check_3cnf
import copy


def generate_estimations(n, i=0, current=[]):
    if (i == n):
        yield current
        return
    for j in range(2):
        for _ in generate_estimations(n, i + 1, current + [j]):
            yield _


def check_sat(phi):
    disjuncts, n = check_3cnf(phi)[1:]
    for est in generate_estimations(n):
        if (run_3cnf(copy.deepcopy(disjuncts), est)):
            return (True, est)
    return (False, None)
