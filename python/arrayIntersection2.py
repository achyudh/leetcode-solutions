class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        index1 = dict()
        for num in nums1:
            if num in index1:
                index1[num] += 1
            else:
                index1[num] = 1
        
        index2 = dict()
        for num in nums2:
            if num in index2:
                index2[num] += 1
            else:
                index2[num] = 1
        
        if len(index1) < len(index2):
            s_index = index1
            l_index = index2
        else:
            l_index = index1
            s_index = index2
        
        intersection = list()
        for num, count in s_index.items():
            if num in l_index:
                for i0 in range(min(s_index[num], l_index[num])):
                    intersection.append(num)
        
        return intersection
