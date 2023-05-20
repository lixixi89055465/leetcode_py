'''
449. 序列化和反序列化二叉搜索树
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑。



示例 1：

输入：root = [2,1,3]
输出：[2,1,3]
示例 2：

输入：root = []
输出：[]


提示：

树中节点数范围是 [0, 104]
0 <= Node.val <= 104
题目数据 保证 输入的树是一棵二叉搜索树。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        def rserialize(node):
            s = []
            if not node:
                return []
            s.append(str(node.val))
            s += rserialize(node.left)
            s += rserialize(node.right)
            return s

        r = rserialize(root)
        s = ','.join(r)
        return s

    def deserialize(self, data):
        def rdeserialize(dataA):
            if dataA[0] == 'N':
                dataA.popleft()
                return
            root = TreeNode(dataA[0])
            dataA.popleft()
            root.left = rdeserialize(dataA)
            root.right = rdeserialize(dataA)
            return root

        dataArray = data.split(',')
        dataArray = deque(dataArray)
        return rdeserialize(dataArray)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
from collections import deque

ser = Codec()
deser = Codec()
# root = [3, 2, 3, None, 3, None, 1]
# root = [3, 4, 5, 1, 3, None, 1]
# root = [3, 9, 20, None, None, 15, 7]
# root = [1]
root = [1, 2, 3, None, None, 4, 5]
# root = []
# root = [1]
# root = [1, 2]
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

tree = ser.serialize(r1)
print(tree)
a = ser.deserialize(tree)
print(a)
