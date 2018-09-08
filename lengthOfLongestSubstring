class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_chars = dict()
        i0 = 0
        max_len = 0
        for i1 in range(len(s)):
            if s[i1] not in current_chars:
                curr_len = i1 - i0 + 1
                if max_len < curr_len:
                    max_len = curr_len
            else:
                for i2 in range(i0, current_chars[s[i1]] + 1):
                    current_chars.pop(s[i2])
                i0 = i2 + 1
            current_chars[s[i1]] = i1
        return max_len
