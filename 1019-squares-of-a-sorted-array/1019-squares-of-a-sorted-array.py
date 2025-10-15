class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        i = 0 

        for i in range(len(nums)-1, -1, -1):
            square = 0
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -=1
            else:
                square = nums[left]
                left+=1
            
            squares[i] = (square*square)
        
        return squares
        