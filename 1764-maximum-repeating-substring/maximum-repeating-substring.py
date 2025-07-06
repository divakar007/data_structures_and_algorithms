class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        n = len(sequence)
        m = len(word)

        k = n//m

        for i in range(1, k+1):
            print(word*i)
            if word*i not in sequence:
                return i-1
        
        return k
        
        