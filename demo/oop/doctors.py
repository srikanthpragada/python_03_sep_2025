from abc import ABC, abstractmethod

class Doctor(ABC):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    @abstractmethod
    def getsalary(self):
        pass


class Resident(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, dept, visits, charge):
        super().__init__(name, dept)
        self.visits = visits
        self.charge = charge

    def getsalary(self):
        return self.visits * self.charge


c = Consultant("Dr. Larry", "card", 10, 2000)
print(c.getsalary())
