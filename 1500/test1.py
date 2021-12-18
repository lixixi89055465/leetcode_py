# a = [1, 4]
# b = [6, 10]
a = [1, 4]
b = [6, 9]
c = [j - i for i, j in zip(a, b)]
result = max(c)
k = 1
mk = 2
for k in range(k, mk):
    index = c.index(min(c))
    if index == mk - 1:
        a.pop()
        b.pop()
    else:
        a.pop(index + 1)
        b.pop(index)
print(a)
print(b)
