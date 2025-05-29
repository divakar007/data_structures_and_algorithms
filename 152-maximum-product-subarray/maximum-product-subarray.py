class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = 1
        currMin = 1
        res = nums[0]

        for num in nums:
            tmp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(tmp, num * currMin, num)

            res = max(res, currMax)
        
        return res