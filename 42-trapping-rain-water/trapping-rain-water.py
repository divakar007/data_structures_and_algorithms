class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        total_water = 0
        left_max = height[0]
        right_max = height[n-1]

        left = 1
        right = n-1

        while(left <= right):

            if left_max <= right_max:
                left_max = max(left_max, height[left])
                total_water += (left_max - height[left])
                left += 1
            else:
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                right -= 1
        
        return total_water
            


            
        