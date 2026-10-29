import unittest
from average import average


class AverageTests(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(average([2, 4, 6]), 4)

    def test_single_value(self):
        self.assertEqual(average([5]), 5)

    def test_empty_input_contract(self):
        with self.assertRaises(ValueError):
            average([])


if __name__ == '__main__':
    unittest.main()
