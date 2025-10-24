from collections import Counter
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        min_counts = Counter(words[0])
        for word in words:
            word_count = Counter(word)
            for char in min_counts.keys():
                min_counts[char] = min(min_counts[char], word_count[char])
        
        output = []
        for key, value in min_counts.items():
            output.extend(key * value)

        return output