class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ranges = []
        start = nums[0]
        end = nums[0]
        for n in nums[1:]:
            if n == end+1:
                end = n
            elif start != end:
                ranges.append("{}->{}".format(start, end))
                start = n
                end = n
            elif start == end:
                ranges.append("{}".format(start))
                start = n
                end = n
        if start == end:
            ranges.append("{}".format(start))
        else:
            ranges.append("{}->{}".format(start, end))
        return ranges
                    
                
            
        