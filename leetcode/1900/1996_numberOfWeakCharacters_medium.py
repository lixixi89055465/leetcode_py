'''
1996. 游戏中弱角色的数量
你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，其中 properties[i] = [attacki, defensei] 表示游戏中第 i 个角色的属性。

如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，如果认为角色 i 弱于 存在的另一个角色 j ，那么 attackj > attacki 且 defensej > defensei 。

返回 弱角色 的数量。



示例 1：

输入：properties = [[5,5],[6,3],[3,6]]
输出：0
解释：不存在攻击和防御都严格高于其他角色的角色。
示例 2：

输入：properties = [[2,2],[3,3]]
输出：1
解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
示例 3：

输入：properties = [[1,5],[10,4],[4,3]]
输出：1
解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。


提示：

2 <= properties.length <= 105
properties[i].length == 2
1 <= attacki, defensei <= 105
'''


class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        p1 = sorted(properties, key=lambda x: (x[0],x[1]))
        p2 = sorted(properties, key=lambda x: (x[1],x[0]))
        # print(p1)
        # print(p2)
        ans = 0
        while len(p1) > 0 and len(p2) > 0:
            if p1[0][0] < p2[-1][0] and p1[0][1] < p2[-1][1]:
                ans += 1
                p2.remove(p1[0])
                p1.pop(0)
            elif p2[0][0] < p1[-1][0] and p2[0][1] < p1[-1][1]:
                ans += 1
                p1.remove(p2[0])
                p2.pop(0)
            else:
                break
        return ans


solution = Solution()
properties = [[1, 5], [10, 4], [4, 3]]
# properties = [[5, 5], [6, 3], [3, 6]]
# properties = [[2,2],[3,3]]
# properties = [[1, 1], [2, 1], [2, 2], [1, 2]]
properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
result = solution.numberOfWeakCharacters(properties)
print(result)
