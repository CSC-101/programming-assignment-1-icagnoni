import data
import hw1
import unittest
from math import sqrt

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_empty_string(self):
        self.assertEqual(hw1.vowel_count(""), 0)

    def test_uppercase_vowels(self):
        self.assertEqual(hw1.vowel_count("AEIOU"), 5)

    # Part 2
    def test_length_2(self):
        self.assertEqual(hw1.short_lists([[1,2], [3, 4]]), [[1, 2], [3, 4]])

    def test_empty_list(self):
        input_data = []
        expected_output = []
        self.assertEqual(hw1.short_lists(input_data), expected_output)

    # Part 3
    def test_mixed_length(self):
        input_data = [[4, 1], [3], [2, 5], [6, 7, 8], [10, 5]]
        expected_output = [[1, 4], [3], [2, 5], [6, 7, 8], [5, 10]]
        self.assertEqual(hw1.ascending_pairs(input_data), expected_output)

    def test_no_length_2(self):
        input_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(hw1.ascending_pairs(input_data), expected_output)

    # Part 4

    def test_add_prices_1(self):
        price1 = hw1.Price(9, 45)
        price2 = hw1.Price(7, 27)
        result = hw1.add_prices(price1, price2)
        self.assertEqual(result.dollars, 16)
        self.assertEqual(result.cents, 72)

    def test_add_prices_2(self):
        price1 = hw1.Price(11, 90)
        price2 = hw1.Price(6, 80)
        result = hw1.add_prices(price1, price2)
        self.assertEqual(result.dollars, 18)
        self.assertEqual(result.cents, 70)


    # Part 5
    def test_Rectangle_1(self):
        top_left = hw1.Point(0,0)
        bottom_right = hw1.Point(1,0)
        rectangle_with_side_equal_zero = hw1.Rectangle(top_left, bottom_right)
        result = hw1.rectangle_area(rectangle_with_side_equal_zero)
        self.assertEqual(result, 0)

    def test_Rectangle_2(self):
        top_left = hw1.Point(3, 6)
        bottom_right = hw1.Point(6, 3)
        rectangle1 = hw1.Rectangle(top_left, bottom_right)
        result = hw1.rectangle_area(rectangle1)
        self.assertEqual(result, 9)


    # Part 6
    def test_books_by_author_1(self):
        authors = ["A", "B", "C"]
        title = "D"
        book1 = hw1.Book(authors, title)
        book2 = hw1.Book(["A", "B"], "Grapes")
        result = hw1.books_by_author("C", [book1, book2])
        self.assertEqual(result, [book1])

    def test_books_by_author_2(self):
        book1 = hw1.Book(["E", "F", "G"], "Guitar")
        book2 = hw1.Book(["E", "F", "G"], "Piano")
        result = hw1.books_by_author("H", [book1, book2])
        self.assertEqual(result, [])

    # Part 7
    def test_circle_1(self):
        circle = data.Circle(data.Point(15, 30), 9.5)
        self.assertEqual(circle.center, data.Point(15, 30))
        self.assertEqual(circle.radius, 9.5)

    def test_circle_2(self):
        circle1 = data.Circle(data.Point(10, 15), 5.3)
        circle2 = data.Circle(data.Point(8, 12), 5.3)
        self.assertNotEqual(circle1, circle2)


    # Part 8
    def test_employee_1(self):
        employee = data.Employee('Jake', 7)
        self.assertEqual(employee.name, 'Jake')
        self.assertEqual(employee.pay_rate, 7)

    def test_employee_2(self):
        employees = []
        result = hw1.below_pay_average(employees)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
