class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = {}
        n = len(wall)
        meets = []
        for row in wall:
            curr = 0
            for idx in row[:len(row)-1]:
                curr+=idx
                if curr not in d:
                    d[curr] = 0
                d[curr]+=1
        mn = float('inf')
        for key in d.keys():
            mn = min(mn,n-d[key])

        if mn == float('inf'):
            return n
        return mn

        







