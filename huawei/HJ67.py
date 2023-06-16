arr = [int(c) for c in input().split(' ')]

permutation = []
# arr = [7, 2, 1, 10]
# arr = [7, 2, 1, 10]
nums = [0, 1, 2, 3]
# arr = [3, 9, 2, 8]
# arr = [9, 3, 8, 2]
for i in nums:
    for j in nums:
        for k in nums:
            for l in nums:
                if i not in [j, k, l] and j not in [k, l] and k != l:
                    permutation.append([arr[i], arr[j], arr[k], arr[l]])


def dfs(arr, index, sum):
    if index == 4:
        return sum == 24

    if index == 0:
        return dfs(arr, index + 1, arr[index])
    if dfs(arr, index + 1, sum + arr[index]) or dfs(arr, index + 1, sum - arr[index]) \
            or dfs(arr, index + 1, sum * arr[index]):
        return True
    return False if sum % arr[index] != 0 else dfs(arr, index + 1, sum // arr[index])


for per in permutation:
    if dfs(per, 0, 0):
        print('true')
        exit(0)
print('false')
# print(dfs(arr, 0, 0))
