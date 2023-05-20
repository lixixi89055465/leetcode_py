'''
222. 完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。



示例 1：


输入：root = [1,2,3,4,5,6]
输出：6
示例 2：

输入：root = []
输出：0
示例 3：

输入：root = [1]
输出：1


提示：

树中节点的数目范围是[0, 5 * 104]
0 <= Node.val <= 5 * 104
题目数据保证输入的树是 完全二叉树


进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？


'''
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        r1 = root
        h = 0
        while r1:
            r1 = r1.left
            h += 1
        left = 2 ** (h - 1)
        right = 2 ** h - 1

        def getMid(m):
            a = []
            while m:
                if m & 1:
                    a.append(1)
                else:
                    a.append(0)
                m >>= 1
            a.reverse()
            return a

        mid = 1
        while left < right:
            mid = (right - left + 1) // 2 + left
            a = getMid(mid)
            r1 = TreeNode()
            r1.right = root
            for i in a:
                if i == 1:
                    r1 = r1.right
                else:
                    r1 = r1.left
            if r1:
                left = mid
            else:
                right = mid - 1

        return left


# root = [1, 2, 3, 4, 5, 6]
# root = [1, 2, 3]
root = [1, 2, 3, 4, 5, 6]
# root = []
# root = [1]
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
result = solve.countNodes(r1)
print(result)
