def dfs(odd, even, visit, matrix, match, o):
    for i in matrix[o]:
        if i in visit:
            continue
        visit.add(i)
        if match[i] < 0 or dfs(odd, even, visit, matrix, match, match[i]):
            match[i] = o
            return True
    return False

n = int(input())
arr = [int(i) for i in input().split(" ")]

def isPrime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

res = [0 for i in arr]
odd = []
even = []
ans = 0
for i in arr:
    if i & 1:
        odd.append(i)
    else:
        even.append(i)
matrix = dict()
for i in range(len(odd)):
    matrix[i] = []
    for j in range(len(even)):
        if isPrime(odd[i] + even[j]):
            matrix[i].append(j)

match = [-1 for _ in range(len(even))]
for i in range(len(odd)):
    visit = set()
    if dfs(odd, even, visit, matrix, match, i):
        ans += 1

print(ans)
