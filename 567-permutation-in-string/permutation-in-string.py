class Solution:
    def checkFreq(self, d1, d2):
        for i in range(26):
            if d1[i] != d2[i]:
                return False
        return True

    def checkInclusion(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False
        
        left = 0
        right = l1-1

        freq1 = [0] * 26
        freq2 = [0] * 26
        for i in range(left, right+1):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        
        while(right < l2):
            if self.checkFreq(freq1, freq2):
                return True
            freq2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
            if right >= l2:
                break
            freq2[ord(s2[right]) - ord('a')] += 1
        
        return False


        
        