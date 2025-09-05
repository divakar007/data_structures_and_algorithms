class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 2
        right = 0
        n = len(nums)

        if n <= 2:
            return n

        for i in range(2, n):
            if nums[i] != nums[left-2]:
                nums[left] = nums[i]
                left += 1

        return left
