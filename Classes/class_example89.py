#This class is an example of


class SportsCompetion:
    """This class describes about the sports"""
    def __init__(self, name, country, price):
        """This is used to initialize the values"""
        self.name = name
        self.country = country
        self.price = price

    def get_name_country(self):
        return "{} {}".format(self.country, self.name)

    def __repr__(self):
        return "Competions: {} held in {} with price {}".format(self.name, self.country, self.price)

    def __str__(self):
        return "{} - {}".format(self.get_name_country(), self.price)

archery = SportsCompetion("Archery","United Kingdom",8000)
print(archery)

print(repr(archery))