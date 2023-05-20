'''
1161. 最大层内元素和
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。



示例 1：



输入：root = [1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
示例 2：

输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
输出：2


提示：

树中的节点数在 [1, 104]范围内
-105 <= Node.val <= 105
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def maxLevelSum(self, root):
        sum = []

        def dfs(node,level):
            if level==len(sum):
                sum.append(node.val)
            else:
                sum[level]+=node.val
            if node.left:
                dfs(node.left,level+1 )
            if node.right:
                dfs(node.right,level+1 )
        dfs(root, 0)
        return sum.index(max(sum)) + 1


solve = Solution()
# root = [1, 7, 0, 7, -8, None, None]
# root=[ TreeNode(1), TreeNode(7), TreeNode(0), TreeNode(7), TreeNode(-8), None,None ]
root = [TreeNode(989), None, TreeNode(10250), TreeNode(98693), TreeNode(-89388), None, None, None, TreeNode(-32127)]
result = solve.maxLevelSum(root)
print(result)
