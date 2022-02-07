'''
99. 恢复二叉搜索树
给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。



示例 1：


输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
示例 2：


输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。


提示：

树上节点的数目在范围 [2, 1000] 内
-231 <= Node.val <= 231 - 1


进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？

通过次数85,201提交次数140,044
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def recoverTree(self, root1) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        root = root1
        q = deque()
        qarr = []
        while root or q:
            while root:
                q.append(root)
                root = root.left
            p = q.pop()
            qarr.append(p.val)
            if p.right:
                root = p.right
        sarr = sorted(qarr)
        s = []
        for u, v in zip(qarr, sarr):
            if u != v:
                s.append(u)
        root = root1
        q = deque()
        while root or q:
            while root:
                q.append(root)
                root = root.left
            p = q.pop()
            # qarr.append(p.val)
            if p.val == s[0]:
                p.val = s[1]
            elif p.val == s[1]:
                p.val = s[0]
            if p.right:
                root = p.right


# root = [3, 1, 4, None, None, 2]
r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(3)
r4 = TreeNode(4)
r3.left = r1
r3.right = r4
r4.left = r2

solve = Solution()
result = solve.recoverTree(r3)
print(result)
