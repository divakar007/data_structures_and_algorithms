class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []
        n = len(candidates)

        def dfs(index, required, curr):
            if index == n:
                if required == 0:
                    result.append(curr)
                return

            if required >= candidates[index]:
                dfs(index, required-candidates[index], curr + [candidates[index]])
            
            dfs(index+1, required, curr)
        
        dfs(0, target, [])

        return result
                
                
