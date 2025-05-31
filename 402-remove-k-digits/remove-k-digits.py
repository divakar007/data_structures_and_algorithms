class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        if k == len(num):
            return "0"
        curr_s = num
        n = len(num)
        stack = []
        ind = 0
        while(k):
            while(k and stack and ind < n and stack[-1] > curr_s[ind]):
                stack.pop(-1)
                k -= 1
            if ind == n:
                break
            stack.append(curr_s[ind])
            ind += 1
        
        while(k):
            if stack:
                stack.pop(-1)
            k -= 1
        if ind == n:
            if stack:
                return str(int("".join(stack)))
            else:
                "0"
        else:
            return str(int("".join(stack) + curr_s[ind:]))

