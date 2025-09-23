# Formal parameters that are mutalbe objects can change actual parameters

def prepend(lst, value):
    lst.insert(0, value)


l = [1,2,3]
prepend(l, 10)
print(l)
