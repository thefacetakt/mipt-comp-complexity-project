import unittest
from solutions.stupid import generate_estimations, check_3sat
from cnf_utils import check_3cnf, run_3cnf


class TestStupidSolution(unittest.TestCase):
    def test_generate_estimations(self):
        self.assertEqual(list(generate_estimations(0)), [[]])
        self.assertEqual(list(generate_estimations(1)), [[0], [1]])
        self.assertEqual(list(generate_estimations(2)),
                         [[0, 0],
                          [0, 1],
                          [1, 0],
                          [1, 1]])
        self.assertEqual(list(generate_estimations(3)),
                         [[0, 0, 0],
                          [0, 0, 1],
                          [0, 1, 0],
                          [0, 1, 1],
                          [1, 0, 0],
                          [1, 0, 1],
                          [1, 1, 0],
                          [1, 1, 1]])

    def if_solution_true(self, phi):
        result = check_3sat(phi)
        self.assertTrue(result[0])
        self.assertTrue(run_3cnf(check_3cnf(phi)[1], result[1]))

    def if_solution_false(self, phi):
        result = check_3sat(phi)
        self.assertFalse(result[0])

    def test_solution(self):
        self.if_solution_true("0|1|10")
        self.if_solution_true("0|0|0")
        self.if_solution_true("~0|~1|10")
        self.if_solution_true("~0|~1|~10&0|1|10")
        self.if_solution_true("~0|~1|~10&0|0|0")
        self.if_solution_false("~0|~0|~0&0|0|0")


if __name__ == '__main__':
    unittest.main()
