class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        coin_dp = [float('inf')] * (amount+1)
        coin_dp[0] = 0
        
        for currAmount in range(1, amount+1):
            for denomination in coins:
                if currAmount - denomination >= 0:
                    coin_dp[currAmount] = min(coin_dp[currAmount], 1 + coin_dp[currAmount-denomination])

        return coin_dp[amount] if coin_dp[amount] != float('inf') else -1       
