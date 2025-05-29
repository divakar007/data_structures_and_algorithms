class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        for index in range(n-1, -1, -1):
            oneIndex = 0
            if s[index] == '0':
                continue

            oneIndex = dp[index + 1]

            twoIndex = 0
            if index != n-1:
                if self.isValid(s[index] + s[index + 1]):
                    twoIndex = dp[index + 2]
            dp[index] = oneIndex + twoIndex

        return dp[0]

    def isValid(self, num):
        return 1 <= int(num) <= 26



        