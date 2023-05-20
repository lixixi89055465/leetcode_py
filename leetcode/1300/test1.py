import functools


def custom_sort(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


a = [2, 4, 5, 7, 3]
a.sort(key=functools.cmp_to_key(custom_sort))
print(a)
