class Solution(object):
    def maximumTotalCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp1 = dp2 = nums.pop(0)                     # <-- 1)

        for n in nums:
            dp1, dp2 = max(dp1, dp2) + n, dp1 - n   # <-- 2)

        return max(dp1, dp2) 