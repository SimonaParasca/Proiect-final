import asyncio
import unittest


# Clasa Calculator cu metode de bază pentru operații matematice
class Calculator:
    # Adună două numere și returnează rezultatul
    def add(self, x, y):
        return x + y

    # Scade două numere și returnează rezultatul
    def subtract(self, x, y):
        return x - y

    # Înmulțește două numere și returnează rezultatul
    def multiply(self, x, y):
        return x * y

    # Împarte două numere și returnează rezultatul
    # Ridică o excepție dacă se încearcă împărțirea la zero
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y


# Clasa pentru manipularea șirurilor de caractere
class StringManipulator:
    # Întoarce un șir de caractere inversat
    def reverse_string(self, s):
        return s[::-1]

    # Transformă un șir de caractere în majuscule
    def uppercase_string(self, s):
        return s.upper()

    # Transformă un șir de caractere în minuscule
    def lowercase_string(self, s):
        return s.lower()

    # Capitalizează primul caracter al unui șir
    def capitalize_string(self, s):
        return s.capitalize()


# Clasa pentru procesarea listelor de numere
class ListProcessor:
    # Calculează suma elementelor din listă
    def sum_list(self, lst):
        return sum(lst)

    # Găsește și returnează valoarea maximă din listă
    def max_list(self, lst):
        return max(lst)

    # Găsește și returnează valoarea minimă din listă
    def min_list(self, lst):
        return min(lst)

    # Calculează și returnează media elementelor din listă
    def avg_list(self, lst):
        return sum(lst) / len(lst) if lst else 0


# Clasa asincronă pentru demonstrarea operațiunilor asincrone
class AsyncProcessor:
    # Funcție asincronă care adună două numere cu o întârziere simulată
    async def async_add(self, x, y):
        await asyncio.sleep(1)  # Așteaptă 1 secundă pentru a simula I/O asincron
        return x + y


# Teste unitare pentru clasa Calculator
class TestCalculator(unittest.TestCase):
    # Pregătirea contextului pentru teste; se execută înaintea fiecărui test
    def setUp(self):
        self.calc = Calculator()

    # Test pentru metoda add
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Test pentru metoda subtract
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    # Test pentru metoda multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)

    # Test pentru metoda divide
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    # Test pentru metoda divide atunci când se împarte la zero
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


# Teste unitare pentru clasa StringManipulator
class TestStringManipulator(unittest.TestCase):
    # Pregătirea contextului pentru teste
    def setUp(self):
        self.manipulator = StringManipulator()

    # Test pentru metoda reverse_string
    def test_reverse_string(self):
        self.assertEqual(self.manipulator.reverse_string("abc"), "cba")

    # Test pentru metoda uppercase_string
    def test_uppercase_string(self):
        self.assertEqual(self.manipulator.uppercase_string("abc"), "ABC")

    # Test pentru metoda lowercase_string
    def test_lowercase_string(self):
        self.assertEqual(self.manipulator.lowercase_string("ABC"), "abc")

    # Test pentru metoda capitalize_string
    def test_capitalize_string(self):
        self.assertEqual(self.manipulator.capitalize_string("abc"), "Abc")


# Teste unitare pentru clasa ListProcessor
class TestListProcessor(unittest.TestCase):
    # Pregătirea contextului pentru teste
    def setUp(self):
        self.processor = ListProcessor()

    # Test pentru metoda sum_list
    def test_sum_list(self):
        self.assertEqual(self.processor.sum_list([1, 2, 3]), 6)

    # Test pentru metoda max_list
    def test_max_list(self):
        self.assertEqual(self.processor.max_list([1, 2, 3]), 3)

    # Test pentru metoda min_list
    def test_min_list(self):
        self.assertEqual(self.processor.min_list([1, 2, 3]), 1)

    # Test pentru metoda avg_list
    def test_avg_list(self):
        self.assertEqual(self.processor.avg_list([1, 2, 3]), 2)


# Teste pentru clasa asincronă folosind unittest.IsolatedAsyncioTestCase
class TestAsyncProcessor(unittest.IsolatedAsyncioTestCase):
    # Test asincron pentru metoda async_add
    async def test_async_add(self):
        processor = AsyncProcessor()
        result = await processor.async_add(1, 2)
        self.assertEqual(result, 3)


# Punctul de intrare pentru rularea testelor unitare
if _name_ == '_main_':
    unittest.main()
