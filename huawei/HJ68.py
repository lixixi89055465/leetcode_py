
num, sort_ = int(input()), int(input())
students = list(input().split() for _ in range(num))
if sort_ == 0:
    students = sorted(students, key = lambda x : int(x[1]), reverse=True)
else:
    students = sorted(students, key = lambda x : int(x[1]), reverse=False)

for i in students:
    print(i[0], i[1])