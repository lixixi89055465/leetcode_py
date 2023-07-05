# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stackP = []
        stackP.append(root)
        while not stackP:
            peek = stackP[-1]
            while peek.left:
                stackP.append(peek.left)
                peek = peek.left
            if not peek.right:
                stackP.append(peek.right)
            else:
                tmp = stackP.pop()
                if tmp == p:
                    break


        pass


s = Solution()
root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
print(s.lowestCommonAncestor(root, p, q))
