class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1

        while(left <= right):
            while(right >= 0 and nums[right] == val):
                right -= 1
            while(left < n and nums[left] != val):
                left += 1
            
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return left
        