class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_ones = 0
        n = len(nums)
        curr_count = 0
        for bit in nums:
            if bit == 1:
                curr_count += 1
            else:
                curr_count = 0
            max_ones = max(max_ones, curr_count)
        
        return max_ones
        