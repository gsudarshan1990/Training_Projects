#This is python program on __enter__ and __exit__

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product({self.name},{self.price})"

    def _move_to_center(self):
        print(f'the product {self} is moved to center')

    def _move_to_side(self):
        print(f'The product {self} is moved to side')

    def __enter__(self):
        print('__enter__ is called')
        self._move_to_center()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ is called')
        self._move_to_side()

with Product('BMW',5000) as p:
    print("This statement is prited")