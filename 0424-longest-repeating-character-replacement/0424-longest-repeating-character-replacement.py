class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0 #state variable
        freq = {}
        l = 0
        for r in range(len(s)): #right
            # add to state
            freq[s[r]] = 1 + freq.get(s[r], 0)
            
            #check if window_len - max_freq has hit size k 
            max_freq = max(freq.values())
            if (r-l +1) - max_freq > k: #means window is too big
                #update answer
                freq[s[l]] -= 1
                l += 1
            max_count = max(r - l+1, max_count)

        return max_count
                
            



        