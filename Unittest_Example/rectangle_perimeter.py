"""
This is contains function which provides the perimeter of the rectangle
"""

def get_perimeter_rectangle(length,breadth):
    if length == 0 or breadth == 0:
        raise ValueError("Value should not be Zero")
    return 2*(length+breadth)