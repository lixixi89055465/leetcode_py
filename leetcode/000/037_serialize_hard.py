'''
剑指 Offer 37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。



示例：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import queue


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        data = ""
        q = queue.Queue()
        q.put(root)
        while q.empty() == False:
            a = q.get()
            if a:
                data += str(a.val) + ","
            else:
                data += "N,"
                continue

            if a and a.left:
                q.put(a.left)
            else:
                q.put(None)
            if a and a.right:
                q.put(a.right)
            else:
                q.put(None)

        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        a = data.split(",")
        a=a[:-1]
        for i in range(len(a)):
            if a[i] == 'N':
                a[i] = None
            elif a[i] == "":
                continue
            else:
                a[i] = TreeNode(int(a[i]))

        left, right = 0, 0
        while left<=right and right < len(a):
            if a[left] is None:
                left+=1
                continue
            right += 1
            a[left].left = a[right]
            right += 1
            a[left].right = a[right]
            left += 1
        return a[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

codec = Codec()
a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a1.left = a2
a1.right = a3
a3.left = a4
a3.right = a5
data = codec.serialize(a1)
data = codec.deserialize(data)
print(data.val)
