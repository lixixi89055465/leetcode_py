'''
103. 二叉树的锯齿形层序遍历
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]


提示：

树中节点数目在范围 [0, 2000] 内
-100 <= Node.val <= 100
通过次数200,151提交次数349,780
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
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

        for i, v in enumerate(ans):
            if i & 1:
                v.reverse()
        return ans


solve = Solution()
root = [3, 9, 20, None, None, 15, 7]
r9 = TreeNode(val=9)
r15 = TreeNode(val=15)
r7 = TreeNode(val=7)
r20 = TreeNode(val=20, left=r15, right=r7)
r3 = TreeNode(val=3, left=r9, right=r20)

result = solve.zigzagLevelOrder(r3)
print(result)
