class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pos_len = neg_len = max_len = 0
        for num in nums:
            if num == 0:
                pos_len = 0
                neg_len = 0
            elif num > 0:
                pos_len += 1
                neg_len = neg_len + 1 if neg_len > 0 else 0
            else:
                temp = pos_len
                pos_len = neg_len + 1 if neg_len > 0 else 0
                neg_len = temp + 1
            max_len = max(max_len, pos_len)
        return max_len
            

        