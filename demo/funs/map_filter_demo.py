def ispositive(n):
    return n > 0

def square(n):
    return n * n

nums = [10, -10, 9, -8, 44, 55, -30]
pos_nums = list(filter(ispositive , nums))

for v, s in zip(pos_nums, map(square, pos_nums)):
    print(v, s)