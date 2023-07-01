# n = int(input())
# A1, A2 = input().split()
# arr = [int(A1), int(A2)]
# while n > 1:
#     _, A2 = input().split()
#     arr.append(int(A2))
#     n -= 1
# arr = [50, 10, 20, 5]
arr = [27, 34, 16, 34]
arrLen = len(arr)

dp = [[100000000000 for i in range(arrLen)] for _ in range(arrLen)]
for i in range(arrLen - 1):
    dp[i][i + 1] = 0

for lenA in range(3, arrLen + 1):
    for i in range(arrLen - lenA + 1):
        for k in range(i + 1, i + lenA - 1):
            dp[i][i + lenA - 1] = min(dp[i][i + lenA - 1],
                                      arr[i] * arr[k] * arr[i + lenA - 1] + dp[i][k] + dp[k][i + lenA - 1]
                                      )
print(dp[0][arrLen - 1])
