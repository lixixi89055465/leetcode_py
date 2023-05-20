'''
652. 寻找重复的子树
给定一棵二叉树 root，返回所有重复的子树。

对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

如果两棵树具有相同的结构和相同的结点值，则它们是重复的。



示例 1：



输入：root = [1,2,3,4,null,2,4,null,null,4]
输出：[[2,4],[4]]
示例 2：



输入：root = [2,1,1]
输出：[[1]]
示例 3：



输入：root = [2,2,2,3,null,3,null]
输出：[[2,3],[3]]


提示：

树中的结点数在[1,10^4]范围内。
-200 <= Node.val <= 200
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def findDuplicateSubtrees(self, root):
        def dfs(node):
            if not node:
                return 0

            tri = (node.val, dfs(node.left), dfs(node.right))
            if tri in seen:
                (tree, index) = seen[tri]
                repeat.add(tree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[tri] = (node, idx)
                return idx

        idx = 0
        seen = dict()
        repeat = set()

        dfs(root)
        return list(repeat)


solve = Solution()


def arrToTree(arr):
    from collections import deque
    q = deque(arr)
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
    root = r1
    return root


root = [1, 2, 3, 4, None, 2, 4, None, None, 4]
# root = [2,1,1]
# root = [2, 2, 2, 3, None, 3, None]
root = arrToTree(root)
result = solve.findDuplicateSubtrees(root)
print(result)
