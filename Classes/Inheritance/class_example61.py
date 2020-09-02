#This is an example of the class


class Employee:
    """This class describes about the Employee"""
    def __init__(self, name, id , salary):
        """This is used to initialize the values"""
        self.employeename = name
        self.employeeid = id
        self.employeesalary = salary

    def calculatePay(self):
        pass

    def __repr__(self):
        return f"Employee({self.employeename},{self.employeeid},{self.employeesalary})"

class FullTimeEmployee(Employee):
    """This class forms a is a relationship with FullTimeEmployee"""
    def __init__(self, stockoptions):
        self.stockoptions = stockoptions

    def calculatePay(self):
        return 250

class ContractEmployee(Employee):
    """This class forms is a relationship with Full Time Employees"""
    def __init__(self, overtimepay):
        self.overtimepay = overtimepay

    def calculatePay(self):
        return 150