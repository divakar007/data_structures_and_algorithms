class Solution(object):
    def canPartition(self, nums):
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        n = len(nums)
        memo = {}  # key: (i, amountLeft), value: True/False

        def dfs(i, rem):
            # base cases
            if rem == 0:
                return True
            if i == n or rem < 0:
                return False

            # memo check
            key = (i, rem)
            if key in memo:
                return memo[key]

            # choice: take nums[i] or skip it
            take = dfs(i+1, rem - nums[i])
            skip = dfs(i+1, rem)

            memo[key] = take or skip
            return memo[key]

        return dfs(0, target)
