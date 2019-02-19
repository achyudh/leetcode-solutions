class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        int_val = 0
        prev_int_val = 1
        for numeral in s[::-1]:
            curr_int_val = to_int[numeral]
            int_val += curr_int_val if curr_int_val >= prev_int_val else -curr_int_val
            prev_int_val = curr_int_val
        return int_val
