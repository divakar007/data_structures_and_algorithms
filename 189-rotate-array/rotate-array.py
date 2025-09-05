class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n

        left, right = 0, n-k-1
        left2, right2 = n-k, n-1

        while(left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        while(left2 < right2):
            nums[left2], nums[right2] = nums[right2], nums[left2]
            left2 += 1
            right2 -= 1
        
        left = 0
        right = n-1
        while(left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            

        