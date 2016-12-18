from tm_iterating import generate_all_tms
from cnf_utils import check_3cnf, run_3cnf
import copy


def check_3sat(phi):
    correct = check_3cnf(phi)
    if not correct[0]:
        return False
    for n in itertools.count():
        tms = 0
        for tm in generate_all_tms():
            tms += 1
            if (tms == n):
                break
            tm = copy.deepcopy(tm)
            for i in range(len(phi)):
                tm.tape[i] = ord(phi[i])
            count = 0
            while (count < n and not tm.next_step()):
                count += 1
            
