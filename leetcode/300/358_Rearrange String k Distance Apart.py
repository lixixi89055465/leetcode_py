from collections import Counter
import heapq


class Solution:
    def rearrangeString(self, words, k):
        _len = len(words)
        word_count = Counter(words)
        que = []
        for c, v in word_count.items():
            que.append((-v, c))
        res = ""
        while que:
            cnt = min(_len, k)
            used = []
            for i in range(cnt):
                if not que:
                    return res
                v, c = heapq.heappop(que)
                res += str(c)
                if -v > 1:
                    used.append((-v + 1, c))
                _len -= 1
            for use in used:
                heapq.heappush(que, use)
        return res


if __name__ == '__main__':
    solution = Solution()
    # word = "aaadbbcc"
    # k = 2
    word = "aaabc"
    k = 3
    result = solution.rearrangeString(word, k)
    print(result)
