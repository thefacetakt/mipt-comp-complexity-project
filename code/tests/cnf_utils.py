import unittest

from cnf_utils import check_3cnf, run_3cnf


class TestCheckCnfUtils(unittest.TestCase):
    def test_check_3cnf(self):
        self.assertTrue(check_3cnf("0|1|10")[0])
        self.assertTrue(check_3cnf("~0|1|10")[0])
        self.assertTrue(check_3cnf("~0|~1|~10")[0])
        self.assertTrue(check_3cnf("0|1|10&0|11|~100")[0])

        self.assertFalse(check_3cnf("0")[0])
        self.assertFalse(check_3cnf("0|1|11")[0])
        self.assertFalse(check_3cnf("lajksdh")[0])
        self.assertFalse(check_3cnf("0|10&11|100")[0])
        self.assertFalse(check_3cnf("")[0])

    def test_run_3cnf(self):
        self.assertTrue(run_3cnf(check_3cnf("0|1|10")[1], [0, 0, 1]))
        self.assertFalse(run_3cnf(check_3cnf("0|1|10")[1], [0, 0, 0]))

        self.assertFalse(run_3cnf(check_3cnf("~0|1|10")[1], [1, 0, 0]))
        self.assertTrue(run_3cnf(check_3cnf("~0|1|10")[1], [1, 0, 1]))
        self.assertTrue(run_3cnf(
            check_3cnf("0|1|10&0|11|~100")[1], [0, 0, 1, 0, 0]))


if __name__ == '__main__':
    unittest.main()
