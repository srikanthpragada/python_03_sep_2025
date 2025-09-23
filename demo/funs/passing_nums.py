# Formal parameters that are immutalbe objects they cannot change actual parameters
def zero(num):
    print(id(num))
    num = 0
    print(id(num))


a = 100
print(id(a))
zero(a)
print(a)


