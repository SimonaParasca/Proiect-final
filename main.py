# Clasele

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

class StringManipulator:
    # Metoda pentru inversarea unui șir de caractere
    def reverse_string(self, s):
        return s[::-1]

    # Metoda pentru transformarea unui șir de caractere în majuscule
    def uppercase_string(self, s):
        return s.upper()
##Scop: Această metodă calculează suma elementelor unei liste.
##Parametri: Primește un singur parametru, lst, care este o listă de numere.
##Funcționalitate: Folosește funcția încorporată sum a Python pentru a calcula suma elementelor din listă.
##Returnare: Returnează valoarea sumei tuturor elementelor din lst
class ListProcessor:
    def sum_list(self, lst):
        return sum(lst)

##Metoda max_list:
##Scop: Această metodă găsește elementul cu cea mai mare valoare dintr-o listă.
##Parametri: La fel ca sum_list, primește o listă de numere lst ca parametru.
##Funcționalitate: Utilizează funcția încorporată max pentru a determina cel mai mare element din listă.
##Returnare: Returnează elementul cu valoarea maximă din lst.
    def max_list(self, lst):
        return max(lst)

# Testele


import unittest
##Această linie importă modulul unittest din Python,
## care este folosit pentru scrierea și rularea testelor unitare.

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
#test_add: Verifică dacă metoda add a clasei Calculator adună corect două numere.
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
##test_subtract: Testează dacă metoda subtract scade corect două numere.
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

class TestStringManipulator(unittest.TestCase):
    def setUp(self):
        self.manipulator = StringManipulator()

    def test_reverse_string(self):
        self.assertEqual(self.manipulator.reverse_string("abc"), "cba")

    def test_uppercase_string(self):
        self.assertEqual(self.manipulator.uppercase_string("abc"), "ABC")

class TestListProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ListProcessor()

    def test_sum_list(self):
        self.assertEqual(self.processor.sum_list([1, 2, 3]), 6)

    def test_max_list(self):
        self.assertEqual(self.processor.max_list([1, 2, 3]), 3)

# Apelarea testelor

if __name__ == '__main__':
    unittest.main()
