def smallest_pos(lst):
    smallest_num = min(lst)
    for idx, v in enumerate(lst):
        if v == smallest_num:
            return (idx, v)


print(smallest_pos([10, 3, 5, 6, 3, 20]))
