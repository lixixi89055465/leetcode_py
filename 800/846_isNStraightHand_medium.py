'''
846. 一手顺子
Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。

给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。



示例 1：

输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
输出：true
解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
示例 2：

输入：hand = [1,2,3,4,5], groupSize = 4
输出：false
解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。


提示：

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length


注意：此题目与 1296 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

'''


class Solution:
    def isNStraightHand(self, hand, groupSize) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        hand.sort()
        ans = []
        for h in hand:
            if len(ans) == 0:
                ans.append([h])
            elif ans[-1][-1] + 1 == h:
                for a in ans:
                    if a[-1] + 1 == h:
                        a.append(h)
                        break
            elif ans[-1][-1] == h:
                ans.append([h])
            else:
                return False
            while ans and len(ans[0]) == groupSize:
                ans = ans[1:]
        return not ans


solve = Solution()
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
# hand = [1, 2, 3, 4, 5]
# groupSize = 4
# hand = [1, 1, 2, 2, 3, 3]
# groupSize = 2
# hand = [1, 1, 2, 2, 3, 3]
# groupSize = 3
# hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
# groupSize = 3
result = solve.isNStraightHand(hand, groupSize)
print(result)