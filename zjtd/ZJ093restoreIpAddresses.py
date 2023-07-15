class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s, pre, index, start, n, res):
            if index * 3 < n - start or n - start < index:
                return
            if index == 1:
                if s[start] == '0' and start != n - 1:
                    return
                if int(s[start:]) < 256:
                    res.add(pre + str(int(s[start:])))
                return
            if s[start] == '0':
                dfs(s, pre + "0.", index - 1, start + 1, n, res)
                return

            for i in range(start + 1, n):
                if int(s[start:i]) > 255:
                    break
                dfs(s, pre + str(int(s[start:i])) + ".", index - 1, i, n, res)

        n = len(s)
        res = set()
        dfs(s, "", 4, 0, n, res)
        return list(res)


solve = Solution()
# s = "25525511135"
s = "0000"
# s = "101023"
s = "0"
print(solve.restoreIpAddresses(s))
