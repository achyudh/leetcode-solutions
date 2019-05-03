class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_ptr = 0
        if len(needle) == 0:
            return 0
        i0 = 0
        while i0 < len(haystack):
            if haystack[i0] == needle[needle_ptr]:
                needle_ptr += 1
                if needle_ptr == len(needle):
                    return i0 - len(needle) + 1
            else:
                i0 = i0 - needle_ptr
                needle_ptr = 0
            i0 += 1
        if needle_ptr == len(needle):
            return len(haystack) - len(needle)
        else:
            return -1
        
