'''
513. 找树左下角的值
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。



示例 1:



输入: root = [2,1,3]
输出: 1
示例 2:



输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7


提示:

二叉树的节点个数的范围是 [1,104]
-231 <= Node.val <= 231 - 1
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def findBottomLeftValue(self, root):
        q = deque()
        qlen = 1
        q.append(root)
        left = root
        while q:
            p = q.popleft()
            qlen -= 1
            if qlen == 0:
                qlen = len(q)
                if p.left:
                    q.append(p.left)
                    qlen += 1
                if p.right:
                    q.append(p.right)
                    qlen += 1
                if qlen > 0:
                    left = q[0]
            else:
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
        return left.val


root = [5, 2, -3]
# root = [5, 2, -5]
root = [1, 2, 3, 4, None, 5, 6, None, None, 7]
# root = [2, 1, 3]
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
result = solve.findBottomLeftValue(r1)
print(result)
