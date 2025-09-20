def issorted(lst):
    pv = lst[0]
    for v in lst[1:]:
        if v < pv:
            return False
        pv = v

    return True


print(issorted([1, 2, 3, 3]), issorted([10, 5, 20, 15]))
