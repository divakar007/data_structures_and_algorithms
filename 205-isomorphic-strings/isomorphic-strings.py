class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        n = len(s)

        char_map = dict()
        char_map_t = dict()

        for ch in range(n):
            if s[ch] in char_map and char_map[s[ch]] != t[ch]:
                    return False

            if t[ch] in char_map_t and char_map_t[t[ch]] != s[ch]:
                return False
            
            char_map_t[t[ch]] = s[ch]
            char_map[s[ch]] = t[ch]
    
        return True
