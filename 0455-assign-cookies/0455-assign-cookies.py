class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        g_idx = 0
        s_idx = 0

        if not g:
            return 0
        
        while g_idx < len(g) and s_idx < len(s):
            if s[s_idx] >= g[g_idx]:
                g_idx += 1
            
            s_idx += 1

        return g_idx
                    
        