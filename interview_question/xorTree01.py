'''

'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


from collections import defaultdict


class Solution:
    def xorTree(self, root, op):
        m = defaultdict(set)
        for o in op:
            m[o[0]].add(o[1])

        def dfs(r, v):
            for i in m[r.val]:
                v ^= i
            r.val = v
            if r.left:
                dfs(r.left, v)
            if r.right:
                dfs(r.right, v)

        dfs(root, 0)
        return root


solve = Solution()
# r2 = TreeNode(2)
# r3 = TreeNode(3)
# r1 = TreeNode(1, r2, r3)
# op=[[2,4],[1,2]]
r3 = TreeNode(3)
r4 = TreeNode(4)
r1 = TreeNode(1, right=r4)
r2 = TreeNode(2, left=r1, right=r3)
op = [[3, 2], [1, 4], [1, 3], [4, 2], [2, 1]]
result = solve.xorTree(r2, op)
print(result)
