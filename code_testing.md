
В ситуации с расчётом среднего могут возникать различные исключительные ситуации, которые важно покрывать тестами.
Ситуации, которые могут стать проблемой, если не настроить тесты:
- Наличие других типов данных, помимо `int` в тестах.
- Подача на вход пустого массива.

Показать недостаточность покрытия кода тестами можно как с помощью конкретных примеров, так и некоторые аспекты можно покрыть теоретически (используя различные комбинации входных данных).
На практике также можно использовать различные метрики для проверки покрытия кода тестами.

Но, разумеется, если недоработки заложены глубоко в логике, то переборы различных входных вариантов могут и не помочь.
В принципе, подобные случае протестировать, кажется, невозможно.


```python
import unittest


class AverageCalculator:

	def calculateAverage(self, numbers: list[int]) -> float:
		if len(numbers) == 0:
			raise AssertionError("Array of numbers can't be empty")
		if not all(type(x) is int for x in numbers):
			raise ValueError("All elements in array must be 'int' type")
		n = len(numbers)
		sum_values = sum(numbers)
		return sum_values / n
		

class TestAverageCalculator(unittest.TestCase):
    def setUp(self):
        self.avg_calculator = AverageCalculator()
        
    def test_default_array(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(self.avg_calculator.calculateAverage(numbers), 2.5)
        
    def test_zeros_array(self):
        numbers = [0, 0, 0, 0, 0]
        self.assertEqual(self.avg_calculator.calculateAverage(numbers), 0)

    def test_all_negative_numbers_array(self):
        numbers = [-5, -2, -3, -10, -15]
        self.assertEqual(self.avg_calculator.calculateAverage(numbers), -7.0)

    def test_nulls_in_array(self):
        with self.assertRaises(ValueError):
            numbers = [4, 1, -2, None, 8]
            self.avg_calculator.calculateAverage(numbers)
	
    def test_empty_array(self):
        with self.assertRaises(AssertionError):
            numbers = []
            self.avg_calculator.calculateAverage(numbers)
	    
     
if __name__ == "__main__":
    unittest.main()

```
