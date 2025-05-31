class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        memo = [[-1] * n for _ in range(amount+1)]
        def waysToMakeChange(curr_amount, index):
            if curr_amount < 0 or index >= n:
                return 0
            if curr_amount == 0:
                return 1

            if memo[curr_amount][index] != -1:
                return memo[curr_amount][index]
            
            pick = waysToMakeChange(curr_amount-coins[index], index)
            notPick = waysToMakeChange(curr_amount, index+1)

            memo[curr_amount][index] = pick+notPick
            return pick + notPick

        return waysToMakeChange(amount, 0)