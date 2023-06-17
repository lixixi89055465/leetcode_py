s = input()
n = int(input())
gc = 0
res = ''
maxGC = 0
for index, c in enumerate(s):
    if index < n:
        if s[index] in 'GC':
            gc += 1
        if maxGC < gc:
            res = s[:n]
            maxGC = gc
        continue
    if s[index - n] in 'GC':
        gc -= 1
    if c in 'GC':
        gc += 1
    if maxGC < gc:
        res = s[index - n + 1:index + 1]
        maxGC = gc

print(res)
