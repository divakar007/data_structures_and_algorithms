class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        all_paranthesis = []
        def solveUtil(curr, opened, closed):
            if opened == closed == n:
                all_paranthesis.append(curr)
                return 
            
            if opened == closed and opened < n:
                solveUtil(curr+'(', opened+1, closed)
            elif opened > closed and opened < n:
                solveUtil(curr+'(', opened+1, closed)
                solveUtil(curr+')', opened, closed+1)
            else:
                solveUtil(curr+')', opened, closed+1)

        solveUtil("", 0, 0)

        return all_paranthesis
            

        