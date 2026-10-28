import unittest
from calculadora_python import somar, subtrair, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(3, 2), 5)
        self.assertEqual(somar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 4), 6)
        self.assertEqual(subtrair(5, 10), -5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(multiplicar(5, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5.0)
        self.assertEqual(dividir(7, 2), 3.5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == "__main__":
    unittest.main()