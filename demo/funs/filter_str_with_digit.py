def has_digit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


values = ['Abc', 'Xyz123', 'PQ1', 'Def3', 'Jef']

for v in filter(has_digit, values):
    print(v)
