class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = {}
        for i, char in enumerate(order):
            order_map[char] = i
        
        for j in range(len(words)-1):
            w1 = words[j]
            w2 = words[j+1]
            for i in range(len(w1)):
                if i == len(w2):
                    return False
                
                if w1[i] != w2[i]:
                    if order_map[w1[i]] < order_map[w2[i]]:
                        break
                    else:
                        return False
        return True             
            
        