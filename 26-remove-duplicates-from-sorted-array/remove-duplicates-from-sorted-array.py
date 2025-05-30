class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr = nums[0]
        left = 0
        right = 0
        while(right < len(nums) and left < len(nums)):
            while(curr == nums[right]):
                right += 1

                if right == len(nums):
                    return left+1
            nums[left+1], nums[right] = nums[right], nums[left+1]
            left += 1
            right += 1
            curr = nums[left]
        
        return left+1
