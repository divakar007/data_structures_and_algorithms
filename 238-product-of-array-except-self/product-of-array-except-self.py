class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        n = len(nums)
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
        
        if zeros >= 2:
            return [0] * n
        if zeros == 1:
            ans = [0] * n
            product = 1
            zeroind = 0
            for ind, i in enumerate(nums):
                if i != 0:
                    product *= i
                else:
                    zeroind = ind
            ans[zeroind] = product
            return ans
        
        product = 1
        
        for ind, num in enumerate(nums):
            product *= num
        
        ans = [0] * n

        for ind, num in enumerate(nums):
            ans[ind] = (product/num)
        
        return ans