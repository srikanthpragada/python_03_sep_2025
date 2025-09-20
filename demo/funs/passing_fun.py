def calltask(task, value):
    print(task(value))


calltask(len, 'abc')
calltask(int, '123')
calltask(print, 100)


