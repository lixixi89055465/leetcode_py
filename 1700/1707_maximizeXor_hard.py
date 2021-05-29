'''
1707. 与数组中元素的最大异或值
给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。

第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。

返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个查询的答案。



示例 1：

输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
输出：[3,3,7]
解释：
1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.
示例 2：

输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
输出：[15,-1,5]


提示：

1 <= nums.length, queries.length <= 105
queries[i].length == 2
0 <= nums[j], xi, mi <= 109
'''


class Tree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.val = None


class Trie:
    def __init__(self, deep=0):
        self.root = Tree()
        self.deep = deep

    def insert(self, ele):
        deep = self.deep
        root = self.root
        while self.deep > 0:
            if (ele >> (len - 1) & 1) == 0:
                if root.left:
                    root = root.left
                else:
                    root.left = Tree()
                    root = root.left
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = Tree()
                    root = root.right
            deep -= 1

    def search(self, ele):
        deep = self.deep
        root = self.root
        val = 0
        while deep > 0:
            if (ele >> (deep - 1) & 1) == 0:
                if root.right and ele < (val + (1 >> (deep - 1))):
                    root = root.right
                    val += (1 >> (deep - 1))
                else:
                    root = root.left
            else:
                if root.left or ele <= (val + (1 >> (deep - 1))):
                    root = root.left
                else:
                    root = root.right
                    val += (1 >> (deep - 1))
            deep -= 1
        return val


class Solution:
    def maximizeXor(self, nums, queries):
        nums = sorted(nums)
        mx = nums[-1]
        deep = 0
        while mx > 0:
            deep += 1
            mx >= 1
        trie = Trie(deep=deep)
        for num in nums:
            trie.insert(num)
        result = []
        for num in queries:
            result.append(trie.search(num[1], num[0]))
        return result


solve = Trie()
nums = []
