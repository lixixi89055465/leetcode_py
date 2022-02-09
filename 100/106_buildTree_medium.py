'''
106. 从中序与后序遍历序列构造二叉树
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。



示例 1:


输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
示例 2:

输入：inorder = [-1], postorder = [-1]
输出：[-1]


提示:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder 和 postorder 都由 不同 的值组成
postorder 中每一个值都在 inorder 中
inorder 保证是树的中序遍历
postorder 保证是树的后序遍历

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not postorder or not inorder:
            return None

        root = TreeNode(postorder[-1])
        for i, v in enumerate(inorder):
            if v == root.val:
                if i != 0:
                    root.left = self.buildTree(inorder[:i], postorder[:i])
                if i != len(inorder) - 1:
                    root.right = self.buildTree(inorder[1 + i:], postorder[i:-1])
                break
        return root


solve = Solution()
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

result = solve.buildTree(inorder, postorder)
print(result)
