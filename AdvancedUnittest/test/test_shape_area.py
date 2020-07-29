from unittest import TestCase
from AdvancedUnittest.src.shape_area import ShapeArea


class TestShape_Area(TestCase):
    def test_triangle_area(self):
         self.assertEqual(ShapeArea.triangle_area(2,6),6)

    def test_square_area(self):
        self.assertEqual(ShapeArea.rectangle_area(10,5),50)

    def test_rectangle_area(self):
        self.assertEqual(ShapeArea.square_area(6),36)
