'''
295. 数据流的中位数
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
'''

import heapq


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.minLen = 0
        self.maxHeap = []
        self.maxLen = 0

    def addNum(self, num: int) -> None:
        if self.minLen == 0:
            heapq.heappush(self.minHeap, -num)
            self.minLen += 1
            return
        if self.maxLen == 0:
            if -self.minHeap[0] > num:
                a = -heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, a)
                heapq.heappush(self.minHeap, -num)
            else:
                heapq.heappush(self.maxHeap, num)
            self.maxLen += 1
            return

        if self.minLen > self.maxLen:
            if -self.minHeap[0] < num:
                heapq.heappush(self.maxHeap, num)
                self.maxLen += 1
            else:
                a = -heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, a)
                heapq.heappush(self.minHeap, -num)
                self.maxLen += 1
        else:
            if self.maxHeap[0] > num:
                heapq.heappush(self.minHeap, -num)
                self.minLen += 1
            else:
                a = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -a)
                heapq.heappush(self.maxHeap, num)
                self.minLen += 1

    def findMedian(self) -> float:
        if self.maxLen > self.minLen:
            return self.maxHeap[0]
        elif self.maxLen < self.minLen:
            return -self.minHeap[0]
        else:
            return (-self.minHeap[0] + self.maxHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# m = obj.findMedian()
# print(m)
# obj.addNum(3)
# m = obj.findMedian()
# print(m)

obj = MedianFinder()
obj.addNum(-1)
m = obj.findMedian()
print(m)
obj.addNum(-2)
m = obj.findMedian()
print(m)
obj.addNum(-3)
m = obj.findMedian()
print(m)
obj.addNum(-4)
m = obj.findMedian()
print(m)
obj.addNum(-5)
m = obj.findMedian()
print(m)
