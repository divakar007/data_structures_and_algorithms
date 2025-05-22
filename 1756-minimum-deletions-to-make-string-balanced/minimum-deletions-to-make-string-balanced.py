class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """        
        if s.count('b') == 0 or s.count('a') == 0:
            return 0
        
        acount = [0] * len(s)
        bcount = [0] * len(s)

        bc = 0
        for i in range(len(s)):
            if s[i] == 'b':
                bcount[i] = bc
                bc += 1
        
        ac = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'b':
                acount[i] = ac
            else:
                ac += 1

        bstart = min(acount[i] + bcount[i] for i in range(len(s)) if s[i] == 'b')

        acount = [0] * len(s)
        bcount = [0] * len(s)

        bc = 0
        for i in range(len(s)):
            if s[i] == 'b':
                bc += 1
            else:
                bcount[i] = bc
        
        ac = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'a':
                acount[i] = ac
                ac += 1

        aend = min(acount[i] + bcount[i] for i in range(len(s)) if s[i] == 'a')

        return min(aend, bstart)
        

        



            
        