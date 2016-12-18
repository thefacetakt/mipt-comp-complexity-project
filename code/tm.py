R = 0
L = 1
N = 2


class Transition:
    def __init__(self, state=0, symbol=0, step=0):
        self.state = state
        self.symbol = symbol
        self.step = step

    def __str__(self):
        return "Transition: " + str((self.state, self.symbol, self.step))


class TwoSidedTape:
    def __init__(self):
        self.front = [ord('#')]
        self.back = [ord('#')]

    def __getitem__(self, i):
        if i >= 0:
            if (i >= len(self.front)):
                self.front.extend([ord('#')] * (i - len(self.front) + 1))
            return chr(self.front[i])
        i = -i - 1
        if i >= len(self.back):
            self.back.extend([ord('#')] * (i - len(self.back) + 1))
        return chr(self.back[i])

    def __setitem__(self, i, x):
        if (isinstance(x, str)):
            x = ord(x)
        self.__getitem__(i)
        if (i >= 0):
            self.front[i] = x
        else:
            self.back[-i - 1] = x

    def __str__(self):
        return ("Tape: " + str(self.back[::-1] + self.front))


class TM:
    def __init__(self, number_of_states):
        self.current_position = 0
        self.current_state = 0
        self.number_of_states = number_of_states
        self.delta = dict()
        self.tape = TwoSidedTape()

    def make_step(self):
        if (self.current_state == self.number_of_states - 1):
            return True
        current_symbol = self.tape[self.current_position]
        transition = self.delta[(self.current_state, current_symbol)]
        self.tape[self.current_position] = transition.symbol
        self.current_state = transition.state
        if (transition.step == R):
            self.current_position += 1
        elif (transition.step == L):
            self.current_position -= 1
        return (self.current_state == self.number_of_states - 1)

    def __str__(self):
        ans = []
        for (k, v) in sorted(list(self.delta.keys())):
            ans += [str((k, v)) + ":" + str(self.delta[(k, v)])]
        return "\n".join(ans) + "\n" + str(self.tape)
