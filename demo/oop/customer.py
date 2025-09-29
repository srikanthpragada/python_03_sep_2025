class Customer:
    def __init__(self, name, email):
        self.name = name
        # private attribute
        self.__email = email

    def getemail(self):
        return self.__email


c = Customer('Larry', 'larry@gmail.com')
print(c.getemail())
print(c.__dict__)  # List of attributes of c
# You can, but should not do this
print(c._Customer__email)

