class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in counter.items()]

        heapq.heapify(maxHeap)

        res = ""
        prev = None

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        
        return res

        