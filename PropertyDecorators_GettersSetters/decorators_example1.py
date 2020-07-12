"""
This is the example of property decorators
"""

class Employee:
    """
    This class describes about the employee
    """
    def __init__(self, name, employee_id, age):
        """
        Initializes the value
        :param name: arg1 and string
        :param employee_id: arg2 and string
        :param age: arg3 and int
        """
        self._name = name
        self._employee_id = employee_id
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, new_employee_id):
        self._employee_id = new_employee_id

    @property
    def age(self):
        return self._age

    def __repr__(self):
        return f"Employee({self.name}, {self.employee_id}, {self.age})"


employee1 = Employee('John',"30001",29)
employee2 = Employee('Jacob', "30002",35)
employee3 = Employee('Johnathan',"30003", 40)

print(employee1)
print(employee2.name)
print(employee3.age)
employee3.employee_id = "30005"
print(employee3.employee_id)
