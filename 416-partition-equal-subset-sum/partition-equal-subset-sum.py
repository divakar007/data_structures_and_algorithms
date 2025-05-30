class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            # walk amounts *down* from target to num
            for amt in range(target, num-1, -1):
                if dp[amt - num]:
                    dp[amt] = True
            if dp[target]:
                return True

        return dp[target]
