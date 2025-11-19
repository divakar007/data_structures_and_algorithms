class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        stack = [(0, -1)]

        maxArea = 0

        for index, height in enumerate(heights):
            
            while stack and (stack[-1][0] > height):
                ht, _ = stack.pop()
                area = (index-stack[-1][1]-1) * ht
                maxArea = max(maxArea, area)

            stack.append((height, index))
        while len(stack) != 1:
            ht, pos = stack.pop()
            area = (n-stack[-1][1]-1) * ht
            maxArea = max(maxArea, area)


        return maxArea