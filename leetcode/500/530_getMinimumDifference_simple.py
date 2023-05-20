'''
530. 二叉搜索树的最小绝对差
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

差值是一个正数，其数值等于两值之差的绝对值。



示例 1：


输入：root = [4,2,6,1,3]
输出：1
示例 2：


输入：root = [1,0,48,null,null,12,49]
输出：1


提示：

树中节点的数目范围是 [2, 104]
0 <= Node.val <= 105

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = []
        q = deque()
        while q or root:
            while root:
                q.append(root)
                root = root.left
            p = q.pop()
            ans.append(p.val)
            if p.right:
                root = p.right
        alen = len(ans)
        mAns = float('inf')
        for i in range(alen - 1):
            mAns = min(mAns, abs(ans[i] - ans[i + 1]))
        return mAns


root = [236, 104, 701, None, 227, None, 911]
q = deque(root)
s = deque()
r1 = TreeNode(q.popleft())
s.append(r1)
while s and q:
    a1 = s.popleft()
    while not a1:
        a1 = s.popleft()
    tmp1 = q.popleft()
    if tmp1:
        a1.left = TreeNode(tmp1)
        s.append(a1.left)
    else:
        s.append(None)
    if not q:
        break
    tmp1 = q.popleft()
    if tmp1:
        a1.right = TreeNode(tmp1)
        s.append(a1.right)
    else:
        s.append(None)
solve = Solution()
result = solve.getMinimumDifference(r1)
print(result)
