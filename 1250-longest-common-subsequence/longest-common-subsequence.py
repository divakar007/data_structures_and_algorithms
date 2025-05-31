class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n1 = len(text1)
        n2 = len(text2)

        memo = [[-1] * n2 for _ in range(n1)]
        def lcs(ind1, ind2):
            if ind1 >= n1 or ind2 >= n2:
                return 0

            if memo[ind1][ind2] != -1:
                return memo[ind1][ind2]
             
            if text1[ind1] == text2[ind2]:
                memo[ind1][ind2] =  1 + lcs(ind1+1, ind2+1)
                return memo[ind1][ind2]

            left = lcs(ind1+1, ind2)
            right = lcs(ind1, ind2+1)
            memo[ind1][ind2] = max(left, right)
            return memo[ind1][ind2]
        
        return lcs(0, 0)
