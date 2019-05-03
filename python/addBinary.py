class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            b0 = [0 for i in range(len(a) - len(b))]
            b0.extend(list(b))
            a = [int(x) for x in a]
            b = [int(x) for x in b0]
        elif len(b) > len(a):
            a0 = [0 for i in range(len(b) - len(a))]
            a0.extend(list(a))
            a = [int(x) for x in a0]
            b = [int(x) for x in b]
        else:
            a = [int(x) for x in a]
            b = [int(x) for x in b]
        c = list()
        carry = 0
        for i0 in range(len(a) - 1, -1, -1):
            c.append(str((a[i0] + b[i0] + carry) % 2))
            carry = (a[i0] + b[i0] + carry) // 2
        if carry == 1:
            c.append(str(carry))
        return "".join(c[::-1])
