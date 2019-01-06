class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev_ssum = set()
        temp = n
        while True:
            ssum = 0
            while temp != 0:
                digit = temp % 10
                ssum += digit * digit
                temp = temp // 10
            if ssum == 1:
                return True
            elif ssum in prev_ssum:
                return False
            else:
                prev_ssum.add(ssum)
                temp = ssum
