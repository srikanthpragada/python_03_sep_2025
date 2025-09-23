
nums = [10, -20, 5, -3, 40, -60, 25]

for n in sorted(nums, key = abs):
    print(n, end = ' ')