'''
993. 二叉树的堂兄弟节点
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。



示例 1：


输入：root = [1,2,3,4], x = 4, y = 3
输出：false
示例 2：


输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true
示例 3：



输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false


提示：

二叉树的节点数介于 2 到 100 之间。
每个节点的值都是唯一的、范围为 1 到 100 的整数。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from queue import Queue


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = Queue()
        q.put(root)
        size1 = 1
        dNum = 1
        dx, dy = 0, 0
        px, py = None, None
        while q.empty() != True:
            tmp = q.get()

            print(tmp.val, size1)
            if tmp.left:
                if tmp.left.val == x:
                    dx = dNum + 1
                    px = tmp
                    if py:
                        break
                if tmp.left.val == y:
                    dy = dNum + 1
                    py = tmp
                    if px:
                        break

                q.put(tmp.left)
            if tmp.right:
                if tmp.right.val == y:
                    dy = dNum + 1
                    py = tmp
                    if px:
                        break
                if tmp.right.val == x:
                    dx = dNum + 1
                    px = tmp
                    if py:
                        break
                q.put(tmp.right)
            size1 -= 1
            if size1 == 0:
                dNum += 1
                size1 = q.qsize()
        if px != py and dx == dy:
            return True
        return False


solve = Solution()
t5 = TreeNode(val=5)
t4 = TreeNode(val=4)
t3 = TreeNode(val=3)
t2 = TreeNode(val=2)
t1 = TreeNode(val=1)

t2.right = t4
t3.right = t5
t1.left = t2
t1.right = t3
result = solve.isCousins(t1, 5, 4)
print(result)
