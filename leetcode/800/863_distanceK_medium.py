'''
863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。



示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1



注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。


提示：

给定的树是非空的。
树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
目标结点 target 是树上的结点。
0 <= K <= 1000.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        elif k > 501:
            return []

        def dfs1(node, path):
            if node == target:
                return path + [node]
            if not node:
                return []
            left = dfs1(node.left, path + [node])
            if left:
                return left
            return dfs1(node.right, path + [node])

        dists = dfs1(root, [])
        parents_distance = dict()
        n = len(dists) - 1
        for i, node in enumerate(dists):
            parents_distance[node] = n - i

        ans = []

        def dfs2(node, dis):
            if not node:
                return
            if node in parents_distance:
                dis = k - parents_distance[node]
            if dis < 0 and not (
                    (node.left and node.left in parents_distance) or (node.right and node.right in parents_distance)):
                return
            if not dis:
                ans.append(node.val)
            dfs2(node.left, dis - 1)
            dfs2(node.right, dis - 1)

        dfs2(root, k)
        return ans






solve = Solution()
root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
target = 5
K = 2

from queue import Queue

def init(root: list, K):
    q = Queue()
    node0 = TreeNode(root[0])
    q.put(node0)
    root = root[1:]
    while q.empty() == False:
        node = q.get()
        if len(root) == 0:
            break
        elif len(root) == 1:
            if root[0] is None:
                node.left = None
            else:
                node.left = TreeNode(root[0])
                q.put(node.left)
            break
        if root[0] is None:
            node.left = None
        else:
            node.left = TreeNode(root[0])
            q.put(node.left)
        if root[1] is None:
            node.right = None
        else:
            node.right = TreeNode(root[1])
            q.put(node.right)
        if node.val == K:
            target = node

        root = root[2:]
    return node0, target


root, target = init(root, target)

result = solve.distanceK(root, target, K)
print(result)
