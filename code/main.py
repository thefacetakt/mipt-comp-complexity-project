from tm_iterating import generate_all_tms
from cnf_utils import check_3cnf, run_3cnf
from solutions import dpll
import itertools
import copy
import time


def check_3sat(phi):
    correct = check_3cnf(phi)
    if not correct[0]:
        return False
    for n in itertools.count(start=1):
        tms = 0
        for tm_item in generate_all_tms():
            tms += 1
            if (tms == n):
                break
            tm = copy.deepcopy(tm_item)
            for i in range(len(phi)):
                tm.tape[i] = ord(phi[i])
            count = 0
            while (count < n and not tm.make_step()):
                count += 1
            if (tm.make_step()):
                est = [0] * correct[2]
                for i in range(len(est)):
                    est[i] = tm.tape[i]
                if (run_3cnf(correct[1], est)):
                    print(tm_item)
                    print(tm)
                    return (True, est)
        if (n >= 2 ** (correct[2]) * correct[2]):
            print("Switching to dpll")
            return dpll.check_3sat(phi)


if __name__ == '__main__':
    phi = input()
    print(check_3sat(phi))
