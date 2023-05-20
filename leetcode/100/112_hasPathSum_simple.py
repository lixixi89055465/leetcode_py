'''
112. 路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。



示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
示例 2：


输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
示例 3：

输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。


提示：

树中节点的数目在范围 [0, 5000] 内
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
    def hasPathSum(self, root, targetSum) -> bool:
        def helper(node, targetS):
            if not node:
                return False
            if node.val == targetS and not (node.left or node.right):
                return True
            return helper(node.left, targetS - node.val) or helper(node.right, targetS - node.val)

        if not root:
            return False
        return helper(root, targetSum)


from collections import deque

solve = Solution()
# targetSum = 2
# root = [3, 9, 20, None, None, 15, 7]
# root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
# targetSum = 22
root = [1, 2]
targetSum = 1

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

result = solve.hasPathSum(r1, targetSum)
print(result)
