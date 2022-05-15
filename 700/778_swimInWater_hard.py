'''
778. 水位上升的泳池中游泳
在一个 n x n 的整数矩阵 grid 中，每一个方格的值 grid[i][j] 表示位置 (i, j) 的平台高度。

当开始下雨时，在时间为 t 时，水池中的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。
假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。返回 你到达坐标方格的右下平台 (n-1, n-1) 所需的最少时间 。



示例 1:



输入: grid = [[0,2],[1,3]]
输出: 3
解释:
时间为0时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
示例 2:



输入: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释: 最终的路线用加粗进行了标记。
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的


提示:

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n2
grid[i][j] 中每个值 均无重复
'''
import heapq


class Solution:
    def swimInWater(self, grid):
        you = []
        bian = []
        bian.append([grid[0][0], 0, 0])
        n = len(grid) * len(grid[0])

        for t in range(n):
            while bian[0][0] <= t:
                if bian[0][0] == grid[-1][-1]:
                    return t
                a = heapq.heappop(bian)
                you.append(a[0])
                if a[1] > 0:
                    if grid[a[1] - 1][a[2]] not in you:
                        heapq.heappush(bian, [grid[a[1] - 1][a[2]], a[1] - 1, a[2]])
                if a[1] < len(grid) - 1:
                    if grid[a[1] + 1][a[2]] not in you:
                        heapq.heappush(bian, [grid[a[1] + 1][a[2]], a[1] + 1, a[2]])
                if a[2] > 0:
                    if grid[a[1]][a[2] - 1] not in you:
                        heapq.heappush(bian, [grid[a[1]][a[2] - 1], a[1], a[2] - 1])
                if a[2] < len(grid) - 1:
                    if grid[a[1]][a[2] + 1] not in you:
                        heapq.heappush(bian, [grid[a[1]][a[2] + 1], a[1], a[2] + 1])

        return 0


solve = Solution()
# grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
grid = [[0,2],[1,3]]
result = solve.swimInWater(grid)
print(result)
