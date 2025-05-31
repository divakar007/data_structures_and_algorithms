class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        coinChangeDp = [[0] * n for i in range(amount+1)]
        
        coinChangeDp[0] = [1] * n

        for curr_amount in range(1, amount+1):
            for index in range(n):
                pick = 0
                if curr_amount >= coins[index]:
                    pick = coinChangeDp[curr_amount-coins[index]][index]
                notPick = coinChangeDp[curr_amount][index-1]
                coinChangeDp[curr_amount][index] = pick+notPick
        return coinChangeDp[amount][n-1]


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