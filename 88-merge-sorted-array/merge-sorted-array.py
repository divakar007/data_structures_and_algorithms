class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ind1, ind2 = m-1, n-1
        right = m+n

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        while(ind1 >= 0 and ind2 >= 0):
            if nums1[ind1] > nums2[ind2]:
                nums1[right-1] = nums1[ind1]
                nums1[ind1] = 0
                ind1 -= 1
            else:
                nums1[right-1] = nums2[ind2]
                ind2 -= 1
            right -= 1
        
        if ind1 < 0:
            for i in range(ind2, -1, -1):
                nums1[right-1] = nums2[i]
                right -= 1

        return
            
        