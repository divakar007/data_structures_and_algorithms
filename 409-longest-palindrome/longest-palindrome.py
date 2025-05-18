class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = defaultdict(int)

        for ch in s:
            hashmap[ch] += 1
        
        count_odd = False
        length = 0
        for key in hashmap:
            if hashmap[key] % 2 == 1:
                if not count_odd:
                    count_odd = True
                    length += hashmap[key]
                else:
                    length += (hashmap[key]-1)
            else:
                length += hashmap[key]
        
        return length