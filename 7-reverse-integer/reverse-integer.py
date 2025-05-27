class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x!=0:
            num=x%10
            n=n*10+num
            x=x//10
        n*=sign
        if n>=2**31-1 or n<=-2**31:
            return 0
        return n
        