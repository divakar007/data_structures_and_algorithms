class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        n = min_length = len(nums)
        if sum(nums) < target:
            return 0

        left = right = 0
        curr_sum = 0
        while(right < n):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        
        return min_length
            
        