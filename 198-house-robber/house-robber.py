class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 1:
            return nums[0]

        prev = nums[0]
        curr = max(nums[1], nums[0])

        for i in range(2, n):
            nxt = max(prev + nums[i], curr)
            curr, prev = nxt, curr
        
        return curr
        
        