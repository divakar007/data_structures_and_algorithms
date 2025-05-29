class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        words = set(wordDict)

        memo = [[-1 for i in range(len(s))] for _ in range(len(s))]
        def dfs(left, right, n, memo):
            if memo[left][right] != -1:
                return memo[left][right]

            if right == n-1:
                if s[left:right+1] in words:
                    memo[left][right] = True
                    return True
                memo[left][right] = False
                return False
            
            option1 = False
            if s[left:right+1] in words:
                option1 = dfs(right+1, right+1, n, memo)
            option2 = dfs(left, right+1, n, memo)

            memo[left][right] = option1 or option2

            return memo[left][right]
        
        return dfs(0, 0, len(s), memo)
            

                
