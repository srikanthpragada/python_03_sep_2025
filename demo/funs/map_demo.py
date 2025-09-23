def square(n):
    return n * n


# for v in map(square, [9, 18, 7, 10, 76]):
#    print(v)

for v in map(lambda n : n * n , [9, 18, 7, 10, 76]):
   print(v)