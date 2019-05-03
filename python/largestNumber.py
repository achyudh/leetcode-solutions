class Solution(object):
        
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return str(int("".join(sorted((str(x) for x in nums), 
                                      cmp=lambda a, b: cmp(a + b, b + a), 
                                      reverse=True))))
