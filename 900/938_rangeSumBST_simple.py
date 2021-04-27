'''
938. 二叉搜索树的范围和
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。



示例 1：


输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32
示例 2：


输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def dfs(self, root: TreeNode, low: int, high: int):
        if root is None:
            return
        if root.left:
            self.dfs(root.left, low, high)
        if root.val <= high and root.val >= low:
            self.sum += root.val
        if root.right:
            self.dfs(root.right, low, high)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.sum


solve = Solution()
n5 = TreeNode(5)
n3 = TreeNode(3)
n18 = TreeNode(18)
n7 = TreeNode(7, n3)
n5 = TreeNode(5, n3, n7)
n15 = TreeNode(15, right=n18)
n10 = TreeNode(10, n5, n15)
low = 7
high = 15
result = solve.rangeSumBST(n10, low, high)
print(result)
