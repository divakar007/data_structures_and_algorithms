class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        neg = 0
        zero = 0
        n = len(nums)
        if n == 0:
            return -10**9+7
        if n == 1:
            return nums[0]
        for i in nums:
            if i == 0:
                zero += 1
            elif i > 0:
                pos += 1
            else:
                neg += 1
        
        if pos == n:
            product = 1
            for i in nums:
                product *= i
            return product
        if zero == 0:
            if neg % 2 == 0:
                curr_product = 1
                for i in nums:
                    curr_product *= i
                return curr_product
    
            prefix_product = [0] * n
            suffix_product = [0] * n
            curr_product = 1
            for i in range(n):
                curr_product *= nums[i]
                prefix_product[i] = curr_product
        
            curr_product = 1
            for j in range(n-1, -1, -1):
                curr_product *= nums[j]
                suffix_product[j] = curr_product
            
            max_product = max(nums)
            neg_inds = []
            for i in range(n):
                if nums[i] < 0:
                    neg_inds.append(i)
            for ind in neg_inds:
                if ind-1 >= 0 :
                    max_product = max(max_product, prefix_product[ind-1])
                if ind + 1 < n:
                    max_product = max(max_product, suffix_product[ind+1])

            return max_product
        else:
            zero_inds = []
            for i in range(n):
                if nums[i] == 0:
                    zero_inds.append(i)
            start = 0
            max_product = max(nums)
            for ind in zero_inds:
                max_product = max(max_product, self.maxProduct(nums[start:ind]))
                start = ind+1
            max_product = max(max_product, self.maxProduct(nums[start:]))
            return max_product