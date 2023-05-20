'''
572. 另一棵树的子树
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。



示例 1：


输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true
示例 2：


输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false


提示：

root 树上的节点数量范围是 [1, 2000]
subRoot 树上的节点数量范围是 [1, 1000]
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def getAll(node):
            q = deque()
            rArr = []
            while q or node:
                while node:
                    q.append(node)
                    node = node.left
                p = q.pop()
                rArr.append(p)
                if p.right:
                    node = p.right
            return rArr

        rArr = getAll(root)
        sArr = getAll(subRoot)
        for i in range(len(rArr) - len(sArr) + 1):
            index = 0
            for j in range(len(sArr)):
                if rArr[i + j].val == sArr[j].val:
                    index += 1
                    continue
                break

            if index == len(sArr):
                return True
        return False


from collections import deque


def getRoot(node):
    q = deque(node)
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
    return r1


r1 = [3, 4, 5, 1, 2]
r2 = [4, 1, 2]
# r1 = [3, 4, 5, 1, 2, None, None, None, None, 1]
# r2 = [4, 1, 2]
r1 = [1, 2, 3]
r2 = [1, 2]
# r1 = [1]
# r2 = [1]
solve = Solution()
r1 = getRoot(r1)
r2 = getRoot(r2)
result = solve.isSubtree(r1, r2)
print(result)
