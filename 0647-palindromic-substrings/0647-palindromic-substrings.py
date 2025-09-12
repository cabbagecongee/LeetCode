class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        strings = list()
        for i in range(len(s)):
            self.helper(s, i, i, i, strings) #odd
            self.helper(s, i, i, i+1, strings) #even
        return len(strings)

    def helper(self, s, mid, left, right, strings):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            substring = s[left:right+1]
            strings.append(substring)
            left -= 1
            right += 1
        
            