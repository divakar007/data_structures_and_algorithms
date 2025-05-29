class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lisdp = [1] * len(nums)
        n = len(nums)
        for curr in range(1,n):
            temp = 0
            for prev in range(curr):
                temp = max(temp, lisdp[prev] if nums[prev] < nums[curr] else 0)
            lisdp[curr] += temp
        return max(lisdp) 