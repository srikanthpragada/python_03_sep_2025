
class Course:
    #static attribute or class attribute
    taxrate = 12

    @staticmethod
    def settaxrate(newrate):
        Course.taxrate = newrate

    def __init__(self, title, fee):
        # object attributes
        self.title = title
        self.fee = fee


    def show(self):
        print(f'Title : {self.title}')
        print(f'Fee   : {self.fee}')

    def getnetfee(self):
        return self.fee  + self.fee * Course.taxrate // 100

Course.settaxrate(10)

c1 = Course("Python", 10000)
c2 = Course("Gen AI", 15000)

print(getattr(c1,'duration', 24))

c1.show()
print(c1.getnetfee())
