class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        n = len(nums)

        if n == 1:
            return nums[0]
        
        def dpSolution(arr):
            n = len(arr)
            dp = [0] * (n+1)
            dp[1] = arr[0]

            for index in range(2, n+1):
                pick = arr[index-1] + dp[index-2]
                notPick = dp[index-1]
                dp[index] = max(pick, notPick)
                
            return dp[n]
        
        return max(dpSolution(nums[1:]), dpSolution(nums[:-1]))
        
        


        