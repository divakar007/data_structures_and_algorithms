class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        left_bits = [0] * 32
        right_bits = [0] * 32

        result_bits = [0] * 32

        for i in range(31, -1, -1):
            left_bits[i] = left%2
            right_bits[i] = right%2
            left //= 2
            right //= 2
        
        for i in range(32):
            if left_bits[i] == right_bits[i]:
                if left_bits[i] == right_bits[i] == 1:
                    result_bits[i] = 1
            else:
                break

        res = 0
        for i in range(32):
            res += (result_bits[i] * (2** (31- i)))
        
        return res



            