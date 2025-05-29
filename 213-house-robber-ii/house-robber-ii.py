class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        n = len(nums)-1

        if n == 0:
            return nums[0]
        
        def robHouseUtil(index, arr, memo):
            if index >= n:
                return 0
            if memo[index] != -1:
                return memo[index]
            pick = arr[index] + robHouseUtil(index+2, arr, memo)
            notPick = robHouseUtil(index+1, arr, memo)
            memo[index] = max(pick, notPick)
            
            return memo[index]

        return max(robHouseUtil(0,nums[1:], [-1] * n), robHouseUtil(0, nums[:-1], [-1] * n))


        