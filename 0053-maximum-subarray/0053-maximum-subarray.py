class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        max_value = nums[0]
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_value = max(curr_sum, max_value)
        
        return max_value