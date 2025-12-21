class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0 #state variable
        freq = {}
        l = 0
        for r in range(len(s)): #right
            # add to state
            if s[r] in freq.keys():
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            
            #check if window_len - max_freq has hit size k 
            max_freq = max(freq.values())
            if (r-l +1) - max_freq > k: #means window is too big
                #update answer
                freq[s[l]] -= 1
                l += 1
            max_count = max(r - l+1, max_count)

        return max_count
                
            



        