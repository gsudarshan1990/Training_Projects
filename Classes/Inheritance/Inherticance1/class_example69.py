"""
This is another example of inheritance which does not inherit the invisible Instance
"""

class P:
    def set_p(self):
        self.x ="class P"

    def print_p(self):
        print(self.x)

class C(P):
    def set_c(self):
        self.x ="Class C"
    def print_c(self):
        print(self.x)

c = C()
c.set_p()
c.print_p()
c.print_c()
c.set_c()
c.print_p()
c.print_c()
