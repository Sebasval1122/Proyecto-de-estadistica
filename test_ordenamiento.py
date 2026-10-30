import random
import unittest

from ordenamiento import ALGORITMOS, mediana, rango


class TestOrdenamiento(unittest.TestCase):
    def test_algoritmos_igual_que_sorted(self):
        casos = [[], [1], [2, 1], [3, 3, 3], [5, 4, 3, 2, 1], list(range(10))]
        casos += [[random.randint(0, 100) for _ in range(random.randint(0, 50))]
                  for _ in range(100)]
        for algoritmo in ALGORITMOS:
            for caso in casos:
                with self.subTest(algoritmo=algoritmo.__name__, caso=caso):
                    self.assertEqual(algoritmo(list(caso)), sorted(caso))

    def test_negativos(self):
        caso = [3, -1, 0, -7, 2, -1]
        for algoritmo in ALGORITMOS:
            with self.subTest(algoritmo=algoritmo.__name__):
                self.assertEqual(algoritmo(list(caso)), sorted(caso))

    def test_mediana_y_rango(self):
        datos = [7, 2, 9, 4, 4, 1, 8, 5]
        self.assertEqual(mediana(datos), 4.5)
        self.assertEqual(mediana([3, 1, 2]), 2)
        self.assertEqual(rango(datos), 8)


if __name__ == "__main__":
    unittest.main()
