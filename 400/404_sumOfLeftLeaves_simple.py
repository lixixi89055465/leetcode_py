'''
404. 左叶子之和
给定二叉树的根节点 root ，返回所有左叶子之和。



示例 1：



输入: root = [3,9,20,null,null,15,7]
输出: 24
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
示例 2:

输入: root = [1]
输出: 0


提示:

节点数在 [1, 1000] 范围内
-1000 <= Node.val <= 1000

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0

        def helper(node, flag):
            if not node:
                return
            helper(node.left, False)
            helper(node.right, True)
            nonlocal ans
            if flag == 0 and not node.left and not node.right:
                ans += node.val

        helper(root, True)
        return ans


from collections import deque

solve = Solution()
# root = [3, 2, 3, None, 3, None, 1]
# root = [3, 4, 5, 1, 3, None, 1]
# root = [3, 9, 20, None, None, 15, 7]
root = [1]
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

result = solve.sumOfLeftLeaves(r1)
print(result)
