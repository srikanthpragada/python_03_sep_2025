def count_digits(st : str) -> int:
    """
    Returns no. of digits in the given string
    :param st: source string
    :return: count of digits
    """
    count = 0
    for c in st:
        if c.isdigit():
            count += 1

    return count

# c = count_digits('Abc123Xyz')
# print(c)


print(count_digits.__doc__)
help(count_digits)