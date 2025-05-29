class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        def decode(index, memo):
            if index == n:
                return 1
            if s[index] == '0':
                return 0

            if memo[index] != -1:
                return memo[index]
            
            oneIndex = 0
            if index+1 != n:
                if s[index+1] != '0':
                    oneIndex = decode(index + 1, memo)
            else:
                oneIndex = decode(index + 1, memo)

            twoIndex = 0
            if index != n-1:
                if self.isValid(s[index] + s[index+1]):
                    twoIndex = decode(index+2, memo)
            memo[index] = oneIndex + twoIndex
            
            return memo[index]
        memo = [-1] * n 
        return decode(0, memo)

    def isValid(self, num):
        return 1 <= int(num) <= 26



        