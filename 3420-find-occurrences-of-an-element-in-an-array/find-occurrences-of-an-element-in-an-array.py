class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """

        occurances = []

        for i in range(len(nums)):
            if nums[i] == x:
                occurances.append(i)
        
        res = []
        for q in queries:
            if q > len(occurances):
                res.append(-1)
            else:
                res.append(occurances[q-1])
        
        return res
        
        