'''
TME2022校园招聘技术研究类/数据类笔试（I） 企业提供原题00:39:27
3/4
[编程题]修剪叶子
时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 256M，其他语言512M

有一棵有个节点的二叉树，其根节点为。修剪规则如下:
1.修剪掉当前二叉树的叶子节点，但是不能直接删除叶子节点
2.只能修剪叶子节点的父节点，修剪了父节点之后，叶子节点也会对应删掉
3.如果想在留下尽可能多的节点前提下，修剪掉所有的叶子节点。请你返回修剪后的二叉树。
有如下二叉树:
1
2
3
4
5
    o
   / \
  o   o
 / \  / \
o  o o   o
修剪过后仅会留下根节点。

输入例子1:
{1,1,1,1,1,1,1}

输出例子1:
{1}

例子说明1:

叶子节点为最下面的4个1节点，但是不能直接修剪，只能修剪中间的2个1，修剪掉之后，只有根节点了


输入例子2:
{1,#,1,#,1,#,1,#,1}

输出例子2:
{1,#,1,#,1}

例子说明2:
退化为一条链了，将最后两个节点删除。
'''


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return TreeNode类
#
class Solution:
    def pruneLeaves(self, root):
        maxLevel = 1

        def dfs(r, level):
            nonlocal maxLevel
            if not r.left and not r.right:
                maxLevel = max(maxLevel, level)
                return
            if r.left:
                dfs(r.left, level + 1)
            if r.right:
                dfs(r.right, level + 1)

        dfs(root, 1)
        if maxLevel <= 2:
            return None

        def delRoot(r, level):
            nonlocal maxLevel
            if level == maxLevel - 2:
                r.left = None
                r.right = None

            if r.left:
                delRoot(r.left, level + 1)
            if r.right:
                delRoot(r.right, level + 1)

        delRoot(root, 1)
        return root


solve = Solution()
t4 = TreeNode(1)
t5 = TreeNode(1)
t6 = TreeNode(1)
t7 = TreeNode(1)
t2 = TreeNode(1, t4, t5)
t3 = TreeNode(1, t6, t7)
t1 = TreeNode(1, t2, t3)

# t5 = TreeNode(1)
# t4 = TreeNode(1, right=t5)
# t3 = TreeNode(1, right=t4)
# t2 = TreeNode(1, right=t3)
# t1 = TreeNode(1, right=t2)
result = solve.pruneLeaves(t1)
print(result)
