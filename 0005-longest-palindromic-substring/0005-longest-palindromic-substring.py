class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        if not s:
            return ""

        #odd middle
        for i in range(len(s)):
            mid = i
            left = i
            right = i
            length = 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right-left-1 > len(longest):
                longest = s[left+1:right]
        
        #even middle
        for i in range(len(s)-1):
            left = i
            right = i+1
            length = 2
            while left >=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                length += right-left
            if right-left-1 > len(longest):
                longest = s[left+1:right]
    
        return longest