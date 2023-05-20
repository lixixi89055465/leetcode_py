'''
116. 填充每个节点的下一个右侧节点指针
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。



示例 1：



输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
示例 2:

输入：root = []
输出：[]


提示：

树中节点的数量在 [0, 212 - 1] 范围内
-1000 <= node.val <= 1000


进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return root
        q = deque()
        qlen = 1
        q.append(root)
        while q:
            r = q.popleft()
            qlen -= 1
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)

            if qlen == 0:
                qlen = len(q)
                if qlen > 1:
                    for i, v in enumerate(q):
                        if i < qlen - 1:
                            q[i].next = q[i + 1]
        return root


from collections import deque

solve = Solution()
root = [1, 2, 3, 4, 5, 6, 7]
q = deque(root)
s = deque()
r1 = Node(q.popleft())
s.append(r1)
while s and q:
    a1 = s.popleft()
    while not a1:
        a1 = s.popleft()
    tmp1 = q.popleft()
    if tmp1:
        a1.left = Node(tmp1)
        s.append(a1.left)
    else:
        s.append(None)
    tmp1 = q.popleft()
    if tmp1:
        a1.right = Node(tmp1)
        s.append(a1.right)
    else:
        s.append(None)

result = solve.connect(r1)
print(result)
