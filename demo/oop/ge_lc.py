import sys

g = (n * n for n in range(1, 10000))
l = [n * n for n in range(1, 10000)]

print(sys.getsizeof(g))
print(sys.getsizeof(l))



