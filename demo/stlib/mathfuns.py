SIZE = 10

def iseven(n):
    return n % 2 == 0


def ispositive(n):
    return n > 0

# run code when module is run as script (directly) and not imported
if __name__ == '__main__':
    print(iseven(10), ispositive(20))
