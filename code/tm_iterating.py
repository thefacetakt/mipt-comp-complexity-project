from tm import TM, Transition, R, L, N
import itertools
import time


symbols = ['0', '1', '~', '&', '|', '#']


def generate_tms(number_of_states, current_position, tm,
                 current_state, current_symbol):
    if (current_symbol == len(symbols)):
        for _ in generate_tms(number_of_states, 1, tm, current_state - 1, 0):
            yield _
        return
    if (current_state == -1):
        yield tm
        return
    elif (current_position == 1):
        for state in range(0, number_of_states):
            tm.delta[(current_state, symbols[current_symbol])] = \
                Transition(state=state)
            for _ in generate_tms(number_of_states, current_position + 1, tm,
                                  current_state, current_symbol):
                yield _
    elif (current_position == 2):
        for symbol in symbols:
            tm.delta[(current_state, symbols[current_symbol])].symbol = \
                symbol
            for _ in generate_tms(number_of_states, current_position + 1, tm,
                                  current_state, current_symbol):
                yield _
    elif (current_position == 3):
        for step in [R, L, N]:
            tm.delta[(current_state, symbols[current_symbol])].step = step
            for _ in generate_tms(number_of_states, 1, tm,
                                  current_state, current_symbol + 1):
                yield _


def generate_all_tms():
    for i in itertools.count(start=2):
        for tm in generate_tms(i, 1, TM(number_of_states=i), i - 1, 0):
            yield tm
