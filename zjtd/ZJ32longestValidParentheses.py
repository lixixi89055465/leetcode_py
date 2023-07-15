class Solution(object):
    def longestValidParentheses2(self, s):
        left, right = 0, 0
        maxLen = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, left * 2)
            elif left < right:
                left, right = 0, 0
        n = len(s)
        left,right=0,0
        for i in range(n - 1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if left == right:
                maxLen = max(maxLen, left * 2)
            elif right < left:
                left, right = 0, 0
        return maxLen

    def longestValidParentheses1(self, s):
        stack = list()
        stack.append(-1)
        n = len(s)
        maxLen = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1])

        return maxLen

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n)]
        for i, c in enumerate(s):
            if c == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2;
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        print(dp)


solve = Solution()
s = ")()())"
print(solve.longestValidParentheses2(s))
