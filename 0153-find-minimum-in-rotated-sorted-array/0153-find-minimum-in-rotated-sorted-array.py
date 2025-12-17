class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = len(nums) - 2
        left = 1
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]
        
        while (right + 1) > left or right != left:
            if nums[right] > nums[right+1]:
                return nums[right+1]
            if nums[left] < nums[left - 1]:
                return nums[left]
            right -= 1
            left += 1
        
        return None



    