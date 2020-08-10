"""
This is another example of the unittest which tests the widget
"""

import unittest
from tkinter import Widget


class TestDefaultWidgetSize(unittest.TestCase):
    """This is used to test the widget size"""
    def test_widget_size(self):
        self.widget = Widget('widget')
        self.assertEqual(self.widget.size(),(50,50))

if __name__ == '__main__':
    unittest.main()
    