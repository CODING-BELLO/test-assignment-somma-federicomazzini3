import unittest
from main import somma

class TestSomma(unittest.TestCase):
    def test_valori(self):
        self.assertEqual(somma(2, 3), 5)
        self.assertEqual(somma(0, 0), 0)
        self.assertEqual(somma(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()