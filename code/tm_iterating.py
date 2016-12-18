from tm import TM, Transition, R, L, N
import itertools
import time


SIGMA = 2


def generate_tms(number_of_states, current_position, tm,
                 current_state, current_symbol):
    print(number_of_states, current_position, tm, current_state,
          current_symbol)
    if (current_state == number_of_states):
        yield tm
        return
    if (current_position == 0):
        for symbol in range(0, SIGMA):
            for _ in generate_tms(number_of_states, current_position + 1, tm,
                                  current_state, symbol):
                yield _
    elif (current_position == 1):
        for state in range(0, number_of_states):
            tm.delta[(current_state, current_symbol)] = Transition(state=state)
            for _ in generate_tms(number_of_states, current_position + 1, tm,
                                  current_state, current_symbol):
                yield _
    elif (current_position == 2):
        for symbol in range(0, SIGMA):
            tm.delta[(current_state, current_symbol)].symbol = symbol
            for _ in generate_tms(number_of_states, current_position + 1, tm,
                                  current_state, current_symbol):
                yield _
    elif (current_position == 3):
        for step in [L, R, N]:
            tm.delta[(current_state, current_symbol)].step = step
            for _ in generate_tms(number_of_states, 0, tm,
                                  current_state + 1, 0):
                yield _


def generate_all_tms():
    for i in itertools.count(start=1):
        print(i)
        for tm in generate_tms(i, 0, TM(number_of_states=i), 0, 0):
            yield tm
