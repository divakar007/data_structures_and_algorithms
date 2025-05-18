class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counts = Counter(nums)

        max_freq = max([counts[x] for x in counts])
        count_freq = defaultdict(list)

        for num in counts:
            count_freq[counts[num]].append(num)
        
        res = []

        for i in range(max_freq, 0, -1):
            for num in count_freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
