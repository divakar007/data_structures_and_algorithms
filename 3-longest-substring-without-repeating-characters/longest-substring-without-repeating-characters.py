class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == "":
            return 0

        max_length = 0
        n = len(s)
        start = 0
        lookup = {}

        for i in range(0, n):
            if s[i] not in lookup:
                lookup[s[i]] = i
            else:
                start = lookup[s[i]] + 1 if lookup[s[i]] + 1 > start else start
                lookup[s[i]] = i
            max_length = max(max_length, i-start+1)
        return max_length