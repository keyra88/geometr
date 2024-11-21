import unittest
import rectangle
import triangle
import circle
import square
import math


class RectangleTestCase(unittest.TestCase):

    def test_area_random_values(self):
        res = rectangle.area(2, 20)
        self.assertEqual(res, 40)

    def test_area_exchanged_values(self):
        res1 = rectangle.area(7, 4)
        res2 = rectangle.area(4, 7)
        self.assertEqual(res1, res2)

    def test_area_zero_values(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_negative_values(self):
        res = rectangle.area(-5, -8)
        self.assertEqual(res, 0)

    def test_perimeter_random_values(self):
        res = rectangle.perimeter(7, 5)
        self.assertEqual(res, 24)

    def test_perimeter_exchanged_values(self):
        res1 = rectangle.perimeter(14, 23)
        res2 = rectangle.perimeter(23, 14)
        self.assertEqual(res1, res2)

    def test_perimeter_zero_values(self):
        res = rectangle.perimeter(0, 5)
        self.assertEqual(res, 0)

    def test_perimeter_negative_values(self):
        res = rectangle.perimeter(-3, 9)
        self.assertEqual(res, 0)


class SquareTestCase(unittest.TestCase):

    def test_area_random_value(self):
        res = square.area(8)
        self.assertEqual(res, 64)

    def test_area_zero_value(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_negative_value(self):
        res = square.area(-17)
        self.assertEqual(res, 0)

    def test_perimeter_random_value(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_zero_value(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative_value(self):
        res = square.perimeter(-3)
        self.assertEqual(res, 0)


class CircleTestCase(unittest.TestCase):

    def test_area_random_value(self):
        res = circle.area(6)
        self.assertEqual(res, 36 * math.pi)

    def test_area_zero_value(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_negative_value(self):
        res = circle.area(-5)
        self.assertEqual(res, 0)

    def test_perimeter_random_value(self):
        res = circle.perimeter(90)
        self.assertEqual(res, 180 * math.pi)

    def test_perimeter_zero_value(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative_value(self):
        res = circle.perimeter(-88)
        self.assertEqual(res, 0)


class TriangleTestCase(unittest.TestCase):

    def test_area_random_values(self):
        res = triangle.area(3, 3)
        self.assertEqual(res, 4.5)

    def test_area_zero_values(self):
        res = triangle.area(4, 0)
        self.assertEqual(res, 0)

    def test_area_negative_values(self):
        res = triangle.area(23, -4)
        self.assertEqual(res, 0)

    def test_perimeter_random_values(self):
        res = triangle.perimeter(3, 5, 4)
        self.assertEqual(res, 12)

    def test_perimeter_exchanged_values(self):
        res1 = triangle.perimeter(8, 12, 20)
        res2 = triangle.perimeter(12, 8, 20)
        self.assertEqual(res1, res2)

    def test_perimeter_inappropriate_values(self):
        res = triangle.perimeter(1, 5, 100)
        self.assertEqual(res, 0)

    def test_perimeter_zero_values(self):
        res = triangle.perimeter(0, 3, 5)
        self.assertEqual(res, 0)

    def test_perimeter_negative_values(self):
        res = triangle.perimeter(-3, 24, 8)
        self.assertEqual(res, 0)


