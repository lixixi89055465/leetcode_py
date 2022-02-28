'''

'''


class Solution:
    def __init__(self):
        pass

    def __init__(self, mem):
        n = (len(mem) - 1) // 2
        self.mem = mem

        def adj(k):
            while k >= 0:
                index = k
                if mem[k * 2] > mem[k]:
                    index = k * 2
                if k * 2 + 1 < len(mem) and mem[k] < mem[k * 2 + 1]:
                    index = k * 2 + 1
                if index != k:
                    self.swap(k, index)
                k -= 1

        for i in range(n, -1, -1):
            self.adj(i)

    def swap(self, left, right):
        tmp = self.mem[left]
        self.mem[left] = self.mem[right]
        self.mem[right] = tmp

    def adj(self, k):
        while k >= 0:
            index = k
            if self.mem[k * 2] > self.mem[k]:
                index = k * 2
            if k * 2 + 1 < len(self.mem) and self.mem[k] < self.mem[k * 2 + 1]:
                index = k * 2 + 1
            if index != k:
                self.swap(k, index)
            k -= 1

    def add(self, k):
        self.mem.append(k)
        n = (len(mem) - 1) // 2
        while n >= 0:
            index = n
            if self.mem[n * 2 + 1] > self.mem[n]:
                index = n * 2 + 1
            if n * 2 + 2 < len(self.mem) and self.mem[n * 2 + 2] > self.mem[n]:
                index = n * 2 + 2
            if index != n:
                self.swap(n, index)
            n = (n - 1) // 2

    def pop(self):
        ans = self.mem[0]
        self.mem[0] = self.mem[-1]
        self.mem = self.mem[:-1]
        n = 0
        while n * 2 + 1 < len(self.mem):
            index = n
            if self.mem[n * 2 + 1] > self.mem[index]:
                index = n * 2 + 1
            if n * 2 + 2 < len(self.mem) and self.mem[n * 2 + 2] > self.mem[index]:
                index = n * 2 + 2
            if index != n:
                self.swap(index, n)
                n = index
            else:
                break
        return ans

mem = [49, 25, 54, 3, 6, 85, 45, 23, 10]
solve = Solution(mem)
solve.add(100)
print(solve.mem)
solve.pop()
print(solve.mem)
solve.pop()
print(solve.mem)
