class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        max_count = 0
        l = 0

        for r in range(len(s)):
            #add to state
            freq[s[r]] = freq.get(s[r], 0) + 1

            #check window
            max_freq = max(freq.values())
            len_str = r - l + 1 

            if len_str - max_freq - k > 0:
                freq[s[l]] -= 1
                l+=1
            
            max_count = max(r-l+1, max_count)
        
        return max_count
            

        