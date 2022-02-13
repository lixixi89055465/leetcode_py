'''
257. 二叉树的所有路径
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。


示例 1：


输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]
示例 2：

输入：root = [1]
输出：["1"]


提示：

树中节点的数目在范围 [1, 100] 内
-100 <= Node.val <= 100

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        ans = []

        def helper(node, ret):
            if not node:
                return
            ret = ret + '->' + str(node.val)
            helper(node.left, ret)
            helper(node.right, ret)
            if not node.left and not node.right:
                ans.append(ret)

        if not root.left and not root.right:
            return [str(root.val)]
        helper(root.left, str(root.val))
        helper(root.right, str(root.val))
        return ans


solve = Solution()
root = [1, 2, 3, None, 5]
result = solve.binaryTreePaths(root)
print(result)
