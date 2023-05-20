'''
501. 二叉搜索树中的众数
给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 任意顺序 返回。

假定 BST 满足如下定义：

结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树


示例 1：


输入：root = [1,null,2,2]
输出：[2]
示例 2：

输入：root = [0]
输出：[0]


提示：

树中节点的数目在范围 [1, 104] 内
-105 <= Node.val <= 105


进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode):
        q = deque()
        maxR = -1
        maxN = -1
        BaseR = -1
        BaseN = -1
        ans = []
        while root or q:
            while root:
                q.append(root)
                root = root.left
            p = q.pop()
            if BaseR == p.val:
                BaseN += 1
                if BaseR != maxR and BaseN > maxN:
                    ans = [BaseR]
                    maxR = BaseR
                    maxN = BaseN
                elif BaseR != maxR and BaseN == maxN:
                    ans.append(BaseR)
                elif BaseR == maxR and BaseN > maxN:
                    maxN = BaseN
            else:
                BaseR = p.val
                BaseN = 1
                if maxN < BaseN:
                    maxR = BaseR
                    maxN = BaseN
                    ans = [maxR]
                elif maxN == BaseN:
                    ans.append(BaseR)

            if p.right:
                root = p.right
        return ans


from collections import deque

# root = [5, 2, 6, None, 4, None, 7]
root = [5, 3, 6, 2, 4]
root = [5, 3, 5, 2, 4]
root = [0]
root = [3, 2, 3, 2, 2, 3, 3, 2]
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
result = solve.findMode(r1)
print(result)
