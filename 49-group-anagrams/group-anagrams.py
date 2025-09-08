class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        d = defaultdict(list)
        
        for i in strs:
            d["".join(sorted(i))].append(i)
        res = []
        for i in d:
            res.append(d[i])
        return res