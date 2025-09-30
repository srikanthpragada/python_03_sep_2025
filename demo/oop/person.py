class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        print("__gt__")
        return self.age > other.age

    def __int__(self):
        return self.age


p1 = Person("Mark", 30)
print(p1, str(p1), p1.__str__())

p2 = Person("Mark", 30)
print(p1 == p2)  # p1.__eq__(p2)

p3 = Person("Jack", 40)
# print(p3 > p2)  # p3.__gt__(p2)
# print(p1 < p2)  # p1.__gt__(p2)

people = [p1, p2, p3]

for p in sorted(people):
    print(p)
