import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(12, -6), 6)
        self.assertEqual(calc.add(-10, -4), -14)

    def test_subtract(self):
        self.assertEqual(calc.subtract(15, 5), 10)
        self.assertEqual(calc.subtract(-14, -5), -9)
        self.assertEqual(calc.subtract(-10, 5), -15)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 6), 12)
        self.assertEqual(calc.multiply(4, 6), 24)
        self.assertEqual(calc.multiply(-3, -10), 30)

    def test_divide(self):
        self.assertEqual(calc.divide(12, 6), 2)
        self.assertEqual(calc.divide(-14, 7), -2)
        self.assertEqual(calc.divide(-20, -5), 4)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(4, 2)


if __name__ == '__main__':
    unittest.main()