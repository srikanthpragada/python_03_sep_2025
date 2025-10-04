lst = [1, 2]

for n in lst:
    print(n)

li = iter(lst)  # lst.__iter__()
print(type(li))

print(next(li))  # li.__next__()
print(next(li))
print(next(li))