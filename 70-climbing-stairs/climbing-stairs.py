class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 1
        curr = 1
        
        for i in range(2, n+1):
            temp = prev + curr
            prev = curr
            curr = temp
        return curr
        