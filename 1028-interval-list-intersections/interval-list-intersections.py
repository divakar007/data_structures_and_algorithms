class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        n = len(firstList)
        m = len(secondList)
        first = 0
        second = 0

        while (first < n and second < m):
            a, b = firstList[first]
            c, d = secondList[second]

            if c<= b and a <= d:
                res.append([max(a, c), min(b, d)])
            
            if b > d:
                second += 1
            elif b < d:
                first += 1
            else:
                first += 1
                second += 1
        return res