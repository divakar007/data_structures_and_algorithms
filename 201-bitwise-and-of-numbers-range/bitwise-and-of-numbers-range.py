class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        bit = 0
        while left != right :
            left = left >> 1
            right = right >> 1
            bit += 1
        return left << bit



            