def ispositive(n):
    return n > 0


nums = [10, -10, 9, -8, 44, 55, -30]

# for n in filter(ispositive, nums):
#     print(n)

for n in filter(lambda v : v > 0, nums):
    print(n)