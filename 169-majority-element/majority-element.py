class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_element = nums[0]
        count = 1
        for ele in nums[1:]:
            if ele == max_element:
                count += 1
            else:
                if count == 0:
                    max_element = ele
                    count += 1
                else:
                    count -= 1
        return max_element


