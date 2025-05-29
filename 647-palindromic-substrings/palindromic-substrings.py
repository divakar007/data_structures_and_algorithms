class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_string = ""
        longest = 0
        n = len(s)
        count = 0
        for i in range(n):
            left = i-1
            right = i+1
            count += 1
            while(left >= 0 and right < n and s[left] == s[right]):
                left -= 1
                right += 1
                count += 1
            
            if right - left - 1 > longest:
                longest = right - left - 1
                longest_string = s[left+1:right]
        
        for i in range(n-1):

            if s[i] == s[i+1]:
                left = i-1
                right = i+2
                count += 1
                while (left >=0 and right < n and s[left] == s[right]):
                    count += 1
                    left -= 1
                    right += 1
                
                if right - left - 1 > longest:
                    longest = right - left - 1
                    longest_string = s[left+1:right]

        return count