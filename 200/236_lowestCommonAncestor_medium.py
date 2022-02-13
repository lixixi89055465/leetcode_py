'''
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”



示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1


提示：

树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        def getPath(node, v):
            path = list()
            visited = defaultdict(int)
            while node or path:
                while node and not visited[node]:
                    path.append(node)
                    node = node.left
                a = path[-1]
                if a.val == v:
                    return path
                if visited[a.right]:
                    visited[a] = 1
                    path.pop()
                elif not a.left and not a.right:
                    visited[a] = 1
                    path.pop()
                elif visited[a.left] and not a.right:
                    visited[a] = 1
                    path.pop()
                elif not a.left or visited[a.left]:
                    node = a.right
            return path

        sp = getPath(root, p.val)
        sq = getPath(root, q.val)

        ans = None
        for i, j in zip(sp, sq):
            if i != j:
                break
            ans = i
        return ans


from collections import deque

solve = Solution()
# root = [3, 1, 4, None, 2]
# root = [6, 2, 8, 1, 4, 7, 9, None, None, 3, 5]
# root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
# p1 = TreeNode(7)
# p2 = TreeNode(1)
# root = [1, 2, 3, None, 4]
# p1 = TreeNode(4)
# p2 = TreeNode(1)

root = [-1, 1, 3, -2, 4, None, None, 8]
p1 = TreeNode(3)
p2 = TreeNode(8)
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

result = solve.lowestCommonAncestor(r1, p1, p2)
print(result)
