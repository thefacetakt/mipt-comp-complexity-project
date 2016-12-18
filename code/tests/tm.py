import unittest
from tm import TM, R, L, N, Transition

MAX_COUNT = 1000


class TestTM(unittest.TestCase):
    def test_tm1(self):
        tm = TM(2)
        tm.delta[(0, '#')] = Transition(1, '1', N)
        count = 0
        while (not tm.make_step() and count < MAX_COUNT):
            count += 1
        self.assertEqual(count, 0)
        self.assertEqual(tm.tape[0], ('1'))
        self.assertEqual(tm.tape[1], ('#'))
        self.assertEqual(tm.tape[-1], ('#'))
        self.assertEqual(tm.current_position, 0)

    def test_tm2(self):
        tm = TM(3)
        tm.delta[(0, '1')] = Transition(1, '~', R)
        tm.delta[(1, '#')] = Transition(2, '&', R)
        tm.tape[0] = ord('1')
        count = 0
        while (not tm.make_step() and count < MAX_COUNT):
            count += 1
        self.assertEqual(count, 1)
        self.assertEqual(tm.tape[0], ('~'))
        self.assertEqual(tm.tape[1], ('&'))
        self.assertEqual(tm.tape[2], ('#'))
        self.assertEqual(tm.tape[-1], ('#'))
        self.assertEqual(tm.current_position, 2)

    def test_tm3(self):
        tm = TM(2)
        tm.delta[(0, '#')] = Transition(0, '~', L)
        tm.delta[(0, '1')] = Transition(1, '0', N)
        tm.tape[-5] = ord('1')
        count = 0
        while (not tm.make_step() and count < MAX_COUNT):
            count += 1
        self.assertEqual(count, 5)
        self.assertEqual(tm.tape[1], ('#'))
        self.assertEqual(tm.tape[0], '~')
        self.assertEqual(tm.tape[-1], '~')
        self.assertEqual(tm.tape[-2], '~')
        self.assertEqual(tm.tape[-3], '~')
        self.assertEqual(tm.tape[-4], '~')
        self.assertEqual(tm.tape[-5], '0')


if __name__ == '__main__':
    unittest.main()
