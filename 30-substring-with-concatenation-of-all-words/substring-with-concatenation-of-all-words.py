class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        res = []
        if len(s) < len(words) * len(words[0]):
            return res
        
        n = len(words)
        wn = len(words[0])
        sn = len(s)

        sorted_words = sorted(words)
        for start in range(sn - n * wn + 1):
            word = s[start:start + n*wn]
            temp = [word[i:wn+i] for i in range(0, n * wn, wn)]
            temp.sort()

            if temp == sorted_words:
                res.append(start)
        
        return res

        

        