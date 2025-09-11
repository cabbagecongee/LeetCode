class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        for i, n in enumerate(s):
            length = 1
            while i+length < len(s) and s[i+length] not in s[i:i+length]:
                length += 1
            longest = max(length, longest)
        return longest