'''
101. 对称二叉树
给你一个二叉树的根节点 root ， 检查它是否轴对称。



示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：


输入：root = [1,2,2,null,3,null,3]
输出：false


提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100


进阶：你可以运用递归和迭代两种方法解决这个问题吗？
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if (not left and right) or (left and not right):
                return False
            if left:
                return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
            return True

        if root:
            return dfs(root.left, root.right)
        return True


solve = Solution()
p = [1, 2, 1]
q = [1, 1, 2]
result = solve.isSameTree(p, q)
print(result)
