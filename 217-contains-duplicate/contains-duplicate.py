class Solution(object):
    def containsDuplicate(self, nums):
        lookup = set()

        for val in nums:
            if val in lookup:
                return True
            lookup.add(val)
        return False
    