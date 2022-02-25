'''
170. 两数之和 III - 数据结构设计
设计一个接收整数流的数据结构，该数据结构支持检查是否存在两数之和等于特定值。

实现 TwoSum 类：

TwoSum() 使用空数组初始化 TwoSum 对象
void add(int number) 向数据结构添加一个数 number
boolean find(int value) 寻找数据结构中是否存在一对整数，使得两数之和与给定的值相等。如果存在，返回 true ；否则，返回 false 。


示例：

输入：
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
输出：
[null, null, null, null, true, false]

解释：
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4，返回 true
twoSum.find(7);  // 没有两个整数加起来等于 7 ，返回 false


提示：

-105 <= number <= 105
-231 <= value <= 231 - 1
最多调用 104 次 add 和 find
'''

from collections import *


class TwoSum:

    def __init__(self):
        self.m = Counter()

    def add(self, number: int) -> None:
        self.m[number] = 1

    def find(self, value: int) -> bool:
        for k in self.m:
            if value - self.m[k] in self.m:
                return True
        return False
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
