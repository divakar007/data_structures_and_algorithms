class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()

        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        
        xor = 0

        for val in count:
            if count[val] == 2:
                xor ^= val
        
        return xor

        