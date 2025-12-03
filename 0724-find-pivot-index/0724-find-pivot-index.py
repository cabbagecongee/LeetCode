class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumLeft = []
        sumRight = []
        running_right = sum(nums)
        running_left = 0
        for i in range(len(nums)):
            running_right -= nums[i]
            if running_left == running_right:
                return i
            sumLeft.append(running_left)
            sumRight.append(running_right)
            running_left += nums[i]
        return -1

        