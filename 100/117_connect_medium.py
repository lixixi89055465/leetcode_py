'''
117. 填充每个节点的下一个右侧节点指针 II
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。



进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


示例：



输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。


提示：

树中的节点数小于 6000
-100 <= node.val <= 100

'''


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node()
        dummy.next = root
        while dummy.next:
            curp = dummy.next
            dummy.next = None
            pre = dummy
            while curp:
                for cur in [curp.left, curp.right]:
                    if cur:
                        pre.next = cur
                        pre = cur
                curp = curp.next
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
