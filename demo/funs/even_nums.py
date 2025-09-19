def print_even_nums(start, end):
    if start % 2 != 0:
        start = start + 1

    for n in range(start, end + 1, 2):
        print(n, end = ' ')


print_even_nums(10, 20)
print_even_nums(11, 25)

