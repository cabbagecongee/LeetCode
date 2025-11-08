class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        if len(s)%2 != 0:
            return False
        
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing:
                if not stack:
                    return False
                item = stack.pop()
                j = closing.index(i)
                if item != opening[j]:
                    return False
                else:
                    pass
        
        if stack:
            return False
        return True
