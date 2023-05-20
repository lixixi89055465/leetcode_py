'''
475. 供暖器
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。



示例 1:

输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
示例 3：

输入：houses = [1,5], heaters = [2]
输出：3


提示：

1 <= houses.length, heaters.length <= 3 * 104
1 <= houses[i], heaters[i] <= 109
'''
import math


class Solution:
    def binarySearch(self, house, heaters):
        left = 0
        right = len(heaters) - 1
        while left < right:
            mid = (right - left + 1) // 2 + left
            if heaters[mid] > house:
                right = mid - 1
            else:
                left = mid
        return left

    def findRadius(self, houses, heaters) -> int:

        if len(heaters) == 1:
            return max(houses[-1] - heaters[0], heaters[0] - houses[0])
        ans = 0
        heaters.sort()
        for house in houses:
            i = self.binarySearch(house, heaters)
            j = i + 1
            left = house - heaters[i] if i >= 0 else float('inf')
            right = heaters[j] - house if j < len(heaters) else float('inf')
            curDistance = min(math.fabs(left), math.fabs(right))
            # curDistance = min(left, right)
            ans = max(ans, curDistance)
        return int(ans)


solve = Solution()
houses = [1, 2, 3]
heaters = [2]
# houses = [1, 2, 3, 4]
# heaters = [1, 4]
# houses = [1,5]
# heaters = [2]
# houses = [282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923]
# heaters = [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612]
houses = [617819336, 399125485, 156091745, 356425228]
heaters = [585640194, 937186357]
result = solve.findRadius(houses, heaters)
print(result)
