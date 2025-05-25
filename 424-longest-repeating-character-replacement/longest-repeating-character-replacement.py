class Solution:
    def characterReplacement(self, s,  k):
        maxlen = 0
        l = 0
        r = 0
        freq = [0] * 26
        n = len(s)
        maxfreq = 0
        while(r < n):
            freq[ord(s[r]) - ord('A')] += 1
            maxfreq = max(maxfreq, freq[ord(s[r]) - ord('A')])
            if r-l+1 - maxfreq <= k:
                maxlen = max(maxlen, r-l+1)
            else:
                freq[ord(s[l]) - ord('A')] -= 1
                l+=1
            r += 1
        
        return maxlen
        