class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        index1 = set(nums1)        
        index2 = set(nums2)

        if len(index1) < len(index2):
            s_index = index1
            l_index = index2
        else:
            l_index = index1
            s_index = index2
        
        intersection = list()
        for num in s_index:
            if num in l_index:
                intersection.append(num)
        
        return intersection
