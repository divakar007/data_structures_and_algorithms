class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sum_of_squares(n)
        return n == 1
        
        
    def sum_of_squares(self, x):
        sum_2 = 0

        while x:
            sum_2 += (x%10)**2
            x //= 10
        return sum_2