class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        scount = Counter(s)
        tcount = Counter(t)

        if len(list(scount.keys())) != len(list(tcount.keys())):
            return False
        for key in scount:
            if key not in tcount:
                return False
            if tcount[key] != scount[key]:
                return False
        
        return True


        