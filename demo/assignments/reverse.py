def reverse(lst):
    l = len(lst)
    half = l // 2
    for i in range(0, half):
        lst[i], lst[l - 1 - i] = lst[l - 1 - i], lst[i]


l = [1, 2, 3, 4, 5, 6]
reverse(l)
print(l)
