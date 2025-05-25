class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n1 = len(s)
        n2 = len(t)

        freqt = defaultdict(int)

        for ch in t:
            freqt[ch] += 1
        
        curr_freq = defaultdict(int)
        left = 0
        right = 0
        matches = 0
        min_length = 10**9
        min_string = ""
        while(right < n1):
            if matches != n2:
                curr_freq[s[right]] += 1
                if s[right] in freqt and curr_freq[s[right]] <= freqt[s[right]]:
                    matches += 1
                
                while matches == n2:
                    if min_length > right-left+1:
                        min_length = right-left+1
                        min_string = s[left:right+1]
                    curr_freq[s[left]] -= 1
                    if s[left] in freqt and curr_freq[s[left]] < freqt[s[left]]:
                        matches -= 1
                    left += 1
                right += 1
        
        return min_string
        