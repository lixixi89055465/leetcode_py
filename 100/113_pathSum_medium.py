'''
113. 路径总和 II
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。



示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
示例 2：


输入：root = [1,2,3], targetSum = 5
输出：[]
示例 3：

输入：root = [1,2], targetSum = 0
输出：[]


提示：

树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum) -> bool:
        ans = []

        def helper(node, targetS, S):
            if not node:
                return False
            if node.val == targetS and not (node.left or node.right):
                S.append(node.val)
                ans.append(S[:])
                S.pop()
                return True

            S.append(node.val)
            left = helper(node.left, targetS - node.val, S)
            S.pop()
            S.append(node.val)
            right = helper(node.right, targetS - node.val, S)
            S.pop()
            return left or right

        if not root:
            return []
        helper(root, targetSum, [])
        return ans


from collections import deque

solve = Solution()
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
targetSum = 22
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
    if q:
        tmp1 = q.popleft()
        if tmp1:
            a1.right = TreeNode(tmp1)
            s.append(a1.right)
        else:
            s.append(None)

result = solve.pathSum(r1, targetSum)
print(result)
