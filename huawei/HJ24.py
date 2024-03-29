'''

HJ24 合唱队
描述
N 位同学站成一排，音乐老师要请最少的同学出列，使得剩下的 K 位同学排成合唱队形。

设
�
K位同学从左到右依次编号为 1，2…，K ，他们的身高分别为
�
1
,
�
2
,
…
,
�
�
T
1
​
 ,T
2
​
 ,…,T
K
​
  ，若存在
�
(
1
≤
�
≤
�
)
i(1≤i≤K) 使得
�
1
<
�
2
<
.
.
.
.
.
.
<
�
�
−
1
<
�
�
T
1
​
 <T
2
​
 <......<T
i−1
​
 <T
i
​
  且
�
�
>
�
�
+
1
>
.
.
.
.
.
.
>
�
�
T
i
​
 >T
i+1
​
 >......>T
K
​
 ，则称这
�
K名同学排成了合唱队形。
通俗来说，能找到一个同学，他的两边的同学身高都依次严格降低的队形就是合唱队形。
例子：
123 124 125 123 121 是一个合唱队形
123 123 124 122不是合唱队形，因为前两名同学身高相等，不符合要求
123 122 121 122不是合唱队形，因为找不到一个同学，他的两侧同学身高递减。

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

注意：不允许改变队列元素的先后顺序 且 不要求最高同学左右人数必须相等

数据范围：
1
≤
�
≤
3000

1≤n≤3000

输入描述：
用例两行数据，第一行是同学的总数 N ，第二行是 N 位同学的身高，以空格隔开

输出描述：
最少需要几位同学出列

示例1
输入：
8
186 186 150 200 160 130 197 200
复制
输出：
4
复制
说明：
由于不允许改变队列元素的先后顺序，所以最终剩下的队列应该为186 200 160 130或150 200 160 130  
'''
n = int(input())
arr = [int(i) for i in input().split(" ")]
s = []
slen = 1
s.append(arr[0])


def gethalfPos(s, left, right, v):
    while left < right:
        mid = left + (right - left) // 2
        if s[mid] == v:
            return mid;
        elif s[mid] < v:
            left = mid + 1
        else:
            right = mid
    return left


fromLeft = [1]
for i in range(1, n):
    if arr[i] > s[-1]:
        s.append(arr[i])
        slen += 1
    else:
        pos = gethalfPos(s, 0, slen - 1, arr[i])
        s[pos] = arr[i]
    fromLeft.append(len(s))
fromRight = [1]
s = []
s.append(arr[-1])
slen = 1
for i in range(n - 2, -1, -1):
    if arr[i] > s[-1]:
        s.append(arr[i])
        slen += 1
    else:
        pos = gethalfPos(s, 0, slen - 1, arr[i])
        s[pos] = arr[i]
    fromRight.append(len(s))
res = 0
for i in range(n):
    res = max(res, fromLeft[i] + fromRight[n - i - 1])
print(n - res + 1)
