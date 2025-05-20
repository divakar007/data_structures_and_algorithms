class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lookup = set(nums)

        starts = set()
        max_count = 0
        for num in lookup:
            if (num-1 not in lookup) and (num-1 not in starts):
                start = num
                starts.add(num)
                count = 1
                while (start+count in lookup):
                    count += 1
                max_count = max(count, max_count)
        
        return max_count
        