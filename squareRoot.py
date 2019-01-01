class Solution:   
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxr = x
        minr = 0
        midr = -1
        while maxr >= minr:
            midr = (maxr + minr) // 2
            midr2 = midr * midr
            if midr2 > x:
                maxr = midr - 1
            else:
                minr = midr + 1
        return maxr
