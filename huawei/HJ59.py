a = input()
for i in a:
    if a.count(i) == 1:
        print(i)
        break
else:
    print(-1)
