class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(" ")
        i = len(words) -1
        while words[i] == "":
            i-=1
        return len(words[i])