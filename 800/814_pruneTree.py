# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self,root):
        if not root:
            return []
        left=self.pruneTree(root.left)
        right=self.pruneTree(root.right)
        if not left and not right and root.val==0:
            return None
        result=TreeNode(root.val)
        if left:
            result.left=left
        if right:
            result.right=right
        return result
