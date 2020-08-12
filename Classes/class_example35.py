"""
We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
"""


class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_string = "%s is a %s %s worth $%.2f"%(self.name, self.color, self.kind, self.value)
        return desc_string

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.value = 60000
print(car1.description())
car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.value = 10000
print(car2.description())