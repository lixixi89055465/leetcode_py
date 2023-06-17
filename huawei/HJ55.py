n = int(input())
count = 0
for i in range(1, n+1):
    if i % 7 == 0:
        count += 1
    elif '7' in str(i):
        count += 1
print(count)
