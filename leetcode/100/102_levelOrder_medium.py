'''
102. 二叉树的层序遍历
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]


提示：

树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = [[]]
        qlen = 1
        while q:
            p = q.popleft()
            ans[-1].append(p.val)
            qlen -= 1
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
            if qlen == 0 and q:
                ans.append([])
                qlen = len(q)

        return ans


solve = Solution()
root = [3, 9, 20, None, None, 15, 7]
result = solve.levelOrder(root)
print(result)
