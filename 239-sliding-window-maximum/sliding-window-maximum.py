class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        right = 0
        dq = deque([])
        res = []
        while(right < n):
            if len(dq) == 0:
                dq.append(right)
            else:
                while(nums[dq[-1]] < nums[right]):
                    dq.pop()

                    if len(dq) == 0:
                        break
                dq.append(right)
                
            
            if right - left + 1 == k:
                res.append(nums[dq[0]])
                left += 1
                if dq[0] < left:
                    dq.popleft()

            right += 1
        
        return res



        