class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        lookup = dict()
        for ind, val in enumerate(nums):
            if target-val in lookup:
                return [lookup[target-val], ind]
            
            if val not in lookup:
                lookup[val] = ind
        


        