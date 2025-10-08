import json

class Course:
    def __init__(self, title, fee):
        # object attributes
        self.title = title
        self.fee = fee

    def show(self):
        print(f'Title : {self.title}')
        print(f'Fee   : {self.fee}')

c = Course("Gen AI", 10000)
print(json.dumps(c.__dict__))

f = open("courses.json", "rt")
courses = json.load(f)
print(courses)

