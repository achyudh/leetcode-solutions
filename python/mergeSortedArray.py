class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        i = 0
        while i1 >= 0 and i2 >= 0:
            i += 1
            if nums1[i1] > nums2[i2]:
                nums1[m+n-i] = nums1[i1]
                i1 -= 1
            else:
                nums1[m+n-i] = nums2[i2]
                i2 -= 1
                
        for i0 in range(i1, -1, -1):
            i += 1
            nums1[m+n-i] = nums1[i0]
        for i0 in range(i2, -1, -1):
            i += 1
            nums1[m+n-i] = nums2[i0]
