class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        n = len(cost)
        def minCostUtil(index, memo):
            if index >= n:
                return 0
            
            if memo[index] != -1:
                return memo[index]
            
            oneStep = cost[index] + minCostUtil(index + 1, memo)
            twoSteps = cost[index] + minCostUtil(index + 2, memo) 

            memo[index] = min(oneStep, twoSteps)
            return memo[index]
        memo = [-1] * n 
        return min(minCostUtil(0, memo), minCostUtil(1, memo)) 


        