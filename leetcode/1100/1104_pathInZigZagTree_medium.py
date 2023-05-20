'''
1104. 二叉树寻路
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。



给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。



示例 1：

输入：label = 14
输出：[1,3,4,14]
示例 2：

输入：label = 26
输出：[1,2,6,10,26]


提示：

1 <= label <= 10^6
'''

import math


class Solution:
    def getIntLen(self, n):
        count = 0
        while n > 0:
            n //= 2
            count += 1
        return count

    def pathInZigZagTree(self, label: int) -> list:
        llen = self.getIntLen(label)
        realLabel = label
        # if llen % 2 == 0:
        #     realLabel = (1 << llen) - label + (1 << llen - 1) - 1
        # result = []
        # result.append(realLabel)
        result = []
        result.append(realLabel)
        if llen % 2 == 0:
            realLabel = (1 << llen) - label + (1 << llen - 1) - 1
        realLabel >>= 1
        llen -= 1
        while llen > 0:
            if llen % 2 == 0:
                result.append((1 << llen) - realLabel + (1 << llen - 1) - 1)
            else:
                result.append(realLabel)
            realLabel >>= 1
            llen -= 1
        result.reverse()
        return result


solve = Solution()
label = 14
# label = 26
result = solve.pathInZigZagTree(label)
print(result)
