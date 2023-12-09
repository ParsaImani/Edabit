class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls, string):
        firstname, lastname, salary = map(str.strip, string.split("-"))
        return cls(firstname, lastname, float(salary))