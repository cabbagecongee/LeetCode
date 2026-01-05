class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy algo for scheduling is to select the events that end as early as possible
        intervals.sort(key=lambda x: x[1])
        res = 0
        prev = intervals[0]
        for i in intervals[1:]:
            if i[0] < prev[1]:
                res += 1
            else:
                prev = i
        
        return res


            
        