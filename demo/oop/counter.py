class Counter:

    def __init__(self, value = 0):
        # object attribute
        self.value = value

    def inc(self, step = 1):
        self.value += step

    def dec(selfs, step = 1):
        if self.value == 0:
            raise ValueError('Counter cannot be negative so decrement is not possible when it is 0')
        self.value -= step

    @property
    def countervalue(self):
        return self.value


c1 = Counter()  # create an object
c1.inc(5)
c1.inc()

print(c1.countervalue)

c2 = Counter(100)
print(c2.countervalue)
