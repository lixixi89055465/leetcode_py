'''
题目描述
设一个 nn 个节点的二叉树 \text{tree}tree 的中序遍历为(1,2,3,\ldots,n)(1,2,3,…,n)，其中数字 1,2,3,\ldots,n1,2,3,…,n 为节点编号。每个节点都有一个分数（均为正整数），记第 ii 个节点的分数为 d_id
i
​
 ，\text{tree}tree 及它的每个子树都有一个加分，任一棵子树 \text{subtree}subtree（也包含 \text{tree}tree 本身）的加分计算方法如下：

\text{subtree}subtree 的左子树的加分 \times× \text{subtree}subtree 的右子树的加分 ++ \text{subtree}subtree 的根的分数。

若某个子树为空，规定其加分为 11，叶子的加分就是叶节点本身的分数。不考虑它的空子树。

试求一棵符合中序遍历为 (1,2,3,\ldots,n)(1,2,3,…,n) 且加分最高的二叉树 \text{tree}tree。要求输出

\text{tree}tree 的最高加分。

\text{tree}tree 的前序遍历。

输入格式
第 11 行 11 个整数 nn，为节点个数。

第 22 行 nn 个用空格隔开的整数，为每个节点的分数

输出格式
第 11 行 11 个整数，为最高加分（Ans \le 4,000,000,000Ans≤4,000,000,000）。

第 22 行 nn 个用空格隔开的整数，为该树的前序遍历。

输入输出样例
输入 #1复制
5
5 7 1 2 10
输出 #1复制
145
3 1 2 4 5
说明/提示
数据规模与约定
对于全部的测试点，保证 1 \leq n< 301≤n<30，节点的分数是小于 100100 的正整数，答案不超过 4 \times 10^94×10
9
 。
'''

# n = int(input())
# s = input()
# s = [int(i) for i in s.split(" ")]
# print(s)
n = 5
s = [5, 7, 1, 2, 10]
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
print(dp)
for l1 in range(2, n):
    for i in range(0, n - l1):
        j = i + l1
        dp[i][i] = s[i]
        dp[i][i + 1] = s[i] + s[i + 1]
        dp[i][j] = dp[i][i] + dp[i + 1][j]
        for k in range(i + 1, j):
            dp[i][j] = max(dp[i][j], dp[i][k - 1] * dp[k + 1][j] + dp[k][k])

print(dp[0][n])
