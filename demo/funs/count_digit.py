def count_digits(st):
    count = 0
    for c in st:
        if c.isdigit():
            count += 1

    return count

c = count_digits('Abc123Xyz')
print(c)

