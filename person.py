from datetime import date

class Person:
    
    name = None
    country = None
    dob = None

    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    def Age(self):
        today = date.today()
        age = today.year - self.dob.year
        return age


obj = Person("kishor", "India", date(1999, 3, 18))

print(obj.Age())