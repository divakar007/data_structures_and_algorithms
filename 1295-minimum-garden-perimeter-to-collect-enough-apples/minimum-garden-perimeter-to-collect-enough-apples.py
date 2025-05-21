class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """

        def find_val(n):
            return (n*(n+1)*(2*n+1))*2
        
        s=1
        e=10**6

        while s<e:
            m = (s+e)//2
            val = find_val(m)
            if val >= neededApples:
                e = m
            else:
                s= m+1

        return e*8

