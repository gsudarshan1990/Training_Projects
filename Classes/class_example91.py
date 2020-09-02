#This python is for the special python functions


class MethodSub:
    def __init__(self, num):
        self.num = num

    def __sub__(self, other):
        return self.num - other.num

num1 = MethodSub(10)
num2 = MethodSub(12)

print(num1 - num2)
