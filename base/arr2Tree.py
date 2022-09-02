from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


targetSum = 22

root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
# q = deque(root)
# s = deque()
# r1 = TreeNode(q.popleft())
# s.append(r1)
# while s and q:
#     a1 = s.popleft()
#     while not a1:
#         a1 = s.popleft()
#     tmp1 = q.popleft()
#     if tmp1:
#         a1.left = TreeNode(tmp1)
#         s.append(a1.left)
#     else:
#         s.append(None)
#     tmp1 = q.popleft()
#     if tmp1:
#         a1.right = TreeNode(tmp1)
#         s.append(a1.right)
#     else:
#         s.append(None)
# root = r1

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

root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
ans=arrToTree(root)
print(ans)
