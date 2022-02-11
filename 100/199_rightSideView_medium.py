'''
199. 二叉树的右视图
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。



示例 1:



输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
示例 2:

输入: [1,null,3]
输出: [1,3]
示例 3:

输入: []
输出: []


提示:

二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        q = deque()
        q.append(root)
        qlen = 1
        ans = [root.val]
        while q:
            p = q.popleft()
            qlen -= 1
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
            if qlen == 0:
                qlen = len(q)
                if qlen:
                    ans.append(q[-1].val)
        return ans


solve = Solution()
root = [1, 2, 3, None, 5, None, 4]

# root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
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
    tmp1 = q.popleft()
    if tmp1:
        a1.right = TreeNode(tmp1)
        s.append(a1.right)
    else:
        s.append(None)
result = solve.rightSideView(r1)
print(result)
