class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """

        def solveUtil(index, prev, ans):
            if index == len(words):
                return ans

            if prev != groups[index]:
                return solveUtil(index+1, groups[index], ans+[words[index]])
            return solveUtil(index+1, prev, ans)
        
        n = len(words)
        res = []
        for i in range(n):
            if groups[i] == 1:
               res = solveUtil(i+1, 1, [words[i]])
               break

        res1 = []
        for i in range(n):
            if groups[i] == 0:
                res1 = solveUtil(i+1, 0, [words[i]])
                break
        
        if len(res) > len(res1):
            return res
        return res1
            
                

            
        