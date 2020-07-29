from unittest import TestCase
from AdvancedUnittest.src import shapearea


class TestShapeArea(TestCase):
    def test_square_area(self):
        self.assertEqual(shapearea.square_area(5), 25)


class TestShapeArea(TestCase):
    def test_rectangle_area(self):
        self.assertEqual(shapearea.rectangle_area(3, 6), 18)


class TestShapeArea(TestCase):
    def test_triangle_area(self):
        self.assertEqual(shapearea.triangle_area(2,6),6)
