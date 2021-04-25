'''
897. 递增顺序搜索树
给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

示例 1：
输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
示例 2：

输入：root = [5,1,7]
输出：[1,null,5,null,7]

'''  # Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.list1 = TreeNode(-1)
        self.right = self.list1

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.increasingBST(root.left)
        self.right.right=root
        self.right=root
        root.left=None
        self.increasingBST(root.right)
        return self.list1.right


solve = Solution()
# n3 = TreeNode(7)
# n2 = TreeNode(1)
# n1 = TreeNode(5, n2, n3)
# [5,3,6,2,4,null,8,1,null,null,null,7,9]
n1=TreeNode(1)
n4=TreeNode(4)
n7=TreeNode(7)
n9=TreeNode(9)
n8=TreeNode(8,n7,n9)
n2=TreeNode(2,n1)
n3=TreeNode(3,n2,n4)
n6=TreeNode(6,None,n8)
n5=TreeNode(5,n3,n6)





n0 = solve.increasingBST(n5)
print(n0.val)
print(n0.right.val)
