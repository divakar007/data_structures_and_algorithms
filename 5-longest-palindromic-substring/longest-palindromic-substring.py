class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_string = ""
        longest = 0
        n = len(s)
        for i in range(n):
            left = i-1
            right = i+1
            while(left >= 0 and right < n and s[left] == s[right]):
                left -= 1
                right += 1
            
            if right - left - 1 > longest:
                longest = right - left - 1
                longest_string = s[left+1:right]
        
        for i in range(n-1):

            if s[i] == s[i+1]:
                left = i-1
                right = i+2

                while (left >=0 and right < n and s[left] == s[right]):
                    left -= 1
                    right += 1
                
                if right - left - 1 > longest:
                    longest = right - left - 1
                    longest_string = s[left+1:right]

        return longest_string 



        