class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = 1
        curr_min = 1
        global_max = max(nums)
        for n in nums:
            tmp = curr_max*n
            curr_max = max(tmp, curr_min*n, n)
            curr_min = min(tmp, curr_min*n, n)
            global_max = max(curr_max, global_max)
        return global_max
                
            
        