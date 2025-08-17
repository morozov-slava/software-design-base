import unittest
from enum import Enum


# Формируем множество допустимых оценок 
class Grades(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    @classmethod
    def has_grade(cls, grade: int) -> bool:
        return grade in cls._value2member_map_


class GradeCalculator:
    def __init__(self, available_grades: type[Grades]):
        # Множество допустимых оценок
        self.available_grades = available_grades

    def calculateAverage(self, grades: list[int]) -> float:
        if not isinstance(grades, list):
            raise TypeError("Array of grades must have 'list' type")
        if len(grades) == 0:
            raise AssertionError("Array of grades can't be empty")

        sum_values = 0
        for grade in grades:
            if not isinstance(grade, int):
                raise TypeError("All grades in array must be 'int' type")
            if not self.available_grades.has_grade(grade):
                raise ValueError("There is not available grade in array")
            sum_values += grade

        return sum_values / len(grades)


class TestGradeCalculator(unittest.TestCase):
    def setUp(self):
        self.grade_calculator = GradeCalculator(Grades)

    def test_default_grades(self):
        grades = [3, 4, 5, 3, 2, 1]
        self.assertEqual(self.grade_calculator.calculateAverage(grades), 3.0)

    def test_not_available_grade(self):
        with self.assertRaises(ValueError):
            grades = [2, 3, 10, 1, 5]
            self.grade_calculator.calculateAverage(grades)

    def test_not_list_input(self):
        with self.assertRaises(TypeError):
            grades = {"one": 1, "two": 2}
            self.grade_calculator.calculateAverage(grades)

    def test_empty_array(self):
        with self.assertRaises(AssertionError):
            grades = []
            self.grade_calculator.calculateAverage(grades)

    def test_float_type_in_array(self):
        with self.assertRaises(TypeError):
            grades = [3, 2, 4.2, 5]
            self.grade_calculator.calculateAverage(grades)

    def test_str_type_in_array(self):
        with self.assertRaises(TypeError):
            grades = [3, 2, "four", 5]
            self.grade_calculator.calculateAverage(grades)


if __name__ == "__main__":
    unittest.main()



