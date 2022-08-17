'''
641. 设计循环双端队列
设计实现双端队列。

实现 MyCircularDeque 类:

MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。


示例 1：

输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
输出
[null, true, true, true, false, 2, true, true, true, 4]

解释
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4



提示：

1 <= k <= 1000
0 <= value <= 1000
insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull  调用次数不大于 2000 次
'''


class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.front = 0
        self.last = 0
        self.cache = [-1] * (k + 1)
        self.count = 0

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count < self.k:
            self.front = (self.front + 1) % (self.k + 1)
            self.cache[self.front] = value
            self.count += 1
            return True
        return False

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count < self.k:
            self.cache[self.last] = value
            self.last = (self.last - 1) % (self.k + 1)
            self.count += 1
            return True
        return False

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.count > 0:
            self.front = (self.front - 1) % (self.k + 1)
            self.count -= 1
            return True
        return False

    def deleteLast(self):
        """
        :rtype: bool

        """
        if self.count > 0:
            self.last = (self.last + 1) % (self.k + 1)
            self.count -= 1
            return True
        return False

    def getFront(self):
        """
        :rtype: int
        """
        if self.count > 0:
            return self.cache[self.front]
        return -1

    def getRear(self):
        """
        :rtype: int
        """
        if self.count>0:
            return self.cache[(self.last+1)%(self.k+1)]
        return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# circularDeque = MyCircularDeque(3)
# print(circularDeque.insertLast(1))
# print(circularDeque.insertLast(2))
# print(circularDeque.insertFront(3))
# print(circularDeque.insertFront(4))
# print(circularDeque.getRear())
# print(circularDeque.isFull())
# print(circularDeque.deleteLast())
# print(circularDeque.insertFront(4))
# print(circularDeque.getFront())
#@22222222222222222222
# ["","","","","",""","","","","getFront"]
# ,,[]]
circularDeque = MyCircularDeque(3)
# insertFront9
print(circularDeque.insertFront(9))
print(circularDeque.getRear())
# insertFront9
print(circularDeque.insertFront(9))
print(circularDeque.getRear())
# insertFront5
print(circularDeque.insertLast(5))
print(circularDeque.getFront())
print(circularDeque.getRear())
print(circularDeque.getFront())
print(circularDeque.insertLast(8))
print(circularDeque.deleteLast())
print(circularDeque.getFront())
