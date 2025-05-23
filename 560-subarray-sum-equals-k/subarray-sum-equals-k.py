class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        prefix_sum_freq = defaultdict(int)
        currsum = 0
        count = 0
        prefix_sum_freq[0] = 1
        for num in nums:
            currsum += num
            count += prefix_sum_freq[currsum-k]
            prefix_sum_freq[currsum] += 1
        return count







        