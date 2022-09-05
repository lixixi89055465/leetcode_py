'''
646. 最长数对链
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。

现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。

给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。



示例：

输入：[[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4]


提示：

给出数对的个数在 [1, 1000] 范围内。
'''


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        a=sorted(pairs,key=lambda i:i[1])
        ans=[]
        for i in a:
            if not ans:
                ans.append(i)
            elif ans[-1][-1]<i[0]:
                ans.append(i)
        return len(ans)





solve = Solution()
pairs = [[1,2], [2,3], [3,4]]
result = solve.findLongestChain(pairs)
print(result)
