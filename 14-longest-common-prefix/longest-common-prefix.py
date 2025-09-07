class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = len(strs[0])
        n = len(strs)
        for i in range(1, n):
            x = 0
            while(x < min(prefix, len(strs[i])) and strs[i][x] == strs[i-1][x]):
                x += 1
            prefix = x
        
        if prefix == 0:
            return ""
        else:
            return strs[0][:prefix]


        