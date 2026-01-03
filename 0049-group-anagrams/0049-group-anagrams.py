class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        anagrams = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagrams.keys():
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
        
        return list(anagrams.values())

