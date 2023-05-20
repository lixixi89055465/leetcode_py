'''
687. 最长同值路径
给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。

两个节点之间的路径长度 由它们之间的边数表示。



示例 1:



输入：root = [5,4,5,1,1,5]
输出：2
示例 2:



输入：root = [1,4,5,4,4,5]
输出：2


提示:

树的节点数的范围是 [0, 104]
-1000 <= Node.val <= 1000
树的深度将不超过 1000
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def longestUnivaluePath(self, root):
        if not root:
            return 0
        maxAns = 0

        def dfs(node):
            nonlocal maxAns
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            ans = 1
            if node.left and node.left.val == node.val:
                ans += left
            if node.right and node.right.val == node.val:
                ans += right
            maxAns = max(ans, maxAns)
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 1
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 1
            return max(left,right)

        dfs(root)
        return maxAns - 1


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


solve = Solution()
# root = [5, 4, 5, 1, 1]
# root = [5, 4, 5, 1, 1,5]
# root = [1,4,5,4,4,5]
# root = [5, 4, 5, 1, 1, None, 5]
root = [1, 2]
root = arrToTree(root)
result = solve.longestUnivaluePath(root)
print(result)
