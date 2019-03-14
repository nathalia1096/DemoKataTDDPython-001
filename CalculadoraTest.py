from unittest import TestCase
from Calculadora import Calculadora


class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacía")

    def test_sumar_unacadena(self):
        self.assertEqual(Calculadora().sumar("1"),1,"Un numero")

    def test_sumar_unacadena(self):
        self.assertEqual(Calculadora().sumar("1"),1,"Un numero")
        self.assertEqual(Calculadora().sumar("2"), 2, "Un numero")
