class Solution:
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        ans = []
        for i in range(m + n - 1):
            if i % 2 == 0:
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
            else:
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while x < m and y >= 0:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    # mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat = [[1,2],[3,4]]
    result = solution.findDiagonalOrder(mat)
    print(result)
