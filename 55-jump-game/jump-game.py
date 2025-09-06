class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        maxReach = nums[0]
        n = len(nums)
        for i in range(1, n):
            if maxReach < i:
                return False
            maxReach = max(maxReach, i + nums[i])
        
        return True
            
        