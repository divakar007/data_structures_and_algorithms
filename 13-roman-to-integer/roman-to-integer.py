class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        value = 0
        n = len(s)
        prev = None
        for i in range(n-1, -1, -1):
            if prev:
                if romans[prev] > romans[s[i]]:
                    value -= romans[s[i]]
                else:
                    value += romans[s[i]]
            else:
                value += romans[s[i]]
            
            prev = s[i]
        
        return value



        