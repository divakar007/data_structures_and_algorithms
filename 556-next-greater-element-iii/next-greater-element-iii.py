class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = [int(d) for d in str(n)]
        length = len(num)
        # 1. Find the first index 'i' from the right where num[i-1] < num[i].
        i = length - 1
        while i > 0 and num[i - 1] >= num[i]:
            i -= 1
        # If no such pivot exists, there is no greater permutation.
        if i == 0:
            return -1

        pivot = i - 1

        # 2. Find the smallest digit in num[i:] that's > num[pivot], searching from the right.
        j = length - 1
        while num[j] <= num[pivot]:
            j -= 1

        # 3. Swap pivot and that digit.
        num[pivot], num[j] = num[j], num[pivot]
        # 4. Reverse the suffix (everything after 'pivot') to get the next smallest arrangement.
        num[i:] = reversed(num[i:])

        # 5. Reconstruct and check 32-bit signed overflow.
        result = int("".join(map(str, num)))
        return result if result <= 2**31 - 1 else -1