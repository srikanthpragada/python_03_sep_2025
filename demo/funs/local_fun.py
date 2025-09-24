g = 100  # Global


def f1():
    a = 10
    global g
    g = 1000
    # Nested function or local function
    def f2():
        b = 20  # Local variable
        nonlocal a
        a = 1
        print(g, a, b)

    f2()
    print(a)


f1()
