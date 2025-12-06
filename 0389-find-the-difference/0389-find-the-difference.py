class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == "":
            return t

        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        for i in range(len(s)):
            if sorted_t[i] != sorted_s[i]:
                return sorted_t[i]
        
        return sorted_t[-1]

        