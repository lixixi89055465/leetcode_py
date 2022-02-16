'''
508. 出现次数最多的子树元素和
给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。



示例 1：



输入: root = [5,2,-3]
输出: [2,-3,4]
示例 2：



输入: root = [5,2,-5]
输出: [2]


提示:

节点数在 [1, 104] 范围内
-105 <= Node.val <= 105
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root):
        from collections import defaultdict
        m = defaultdict(int)

        def helper(node):
            if node:
                nonlocal m
                left = helper(node.left)
                right = helper(node.right)
                ans = left + right + node.val
                m[ans] += 1
                return ans
            return 0

        helper(root)
        maxV = float('-inf')
        ans = []
        for k in m:
            if m[k] > maxV:
                maxV = m[k]
                ans = [k]
            elif m[k] == maxV:
                ans.append(k)
        return ans


from collections import deque

root = [5, 2, -3]
# root = [5, 2, -5]
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
result = solve.findFrequentTreeSum(r1)
print(result)
