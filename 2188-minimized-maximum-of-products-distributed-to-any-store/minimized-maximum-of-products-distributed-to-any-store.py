class Solution:
    def minimizedMaximum(self, n, quantities):
        def condition(k):
            return sum([ceil(floor(q)/k) for q in quantities]) <= n

        
        if n == len(quantities):
            return max(quantities)

        left, right = 1, max(quantities)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
        


