class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def solveUtil(index, memo):
            if index >= n-1:
                return 0

            if memo[index] != -1:
                return memo[index]
            
            min_steps = float('inf')
            for i in range(1, nums[index]+1):
                min_steps = min(min_steps, 1+solveUtil(index+i, memo))

            memo[index] = min_steps
            return memo[index]
        
        memo = [-1] * n
        return solveUtil(0, memo)

