import unittest
import calculacomplexnumber as lva

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        c1 = (-10.2,1)
        c2 = (-5,8)
        self.assertEqual(lva.sumar(c1,c2),(-15.2,9))

    def test_upper(self):
        c1 = (3, 4)
        c2 = (2, -5)
        self.assertEqual(lva.multiplicar(c1, c2), (26, -7))

    def test_upper(self):
        c1 = (-10.2, -8)
        c2 = (5, 2)
        self.assertEqual(lva.resta(c1, c2), (-5.2, -10))

    def test_upper(self):
        c1 = (-10.2, 1)
        c2 = (-5, 8)
        self.assertEqual(lva.dividir(c1, c2), (0.513, 0.045))

    def test_upper(self):
        c1 = (-500, 2/3)
        self.assertEqual(lva.modulo(c1),500.000)

    def test_upper(self):
        c1 = (-10.2, -5/4)
        self.assertEqual(lva.conjugado(c1),(-10.2,5/4))

    def test_upper(self):
        c1 = (-10.2, 35)
        self.assertEqual(lva.polaracartesiana(c1), (9.217, 4.367))

    def test_upper(self):
        c1 = (-10.2, 9)
        self.assertEqual(lva.fase(c1),-0.72)


if __name__ == '__main__':
    unittest.main()