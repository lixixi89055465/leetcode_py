a = ""


def concat(a, b, k):
    if a == "":
        return str(b)
    for i in range(len(a)):
        if a[i] < str(b):
            return a[:i] + str(b) * k + a[i:]
    return a + str(b) * k


def maxC(c1, c2):
    if len(c1) > len(c2):
        return c1
    elif len(c1) < len(c2):
        return c2
    if c1 > c2:
        return c1
    return c2


a = "432"
b = 3
print(concat(a, 3, 3))
