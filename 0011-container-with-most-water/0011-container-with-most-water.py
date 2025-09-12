class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height or len(height)==1:
            return 0
        if len(height) == 2:
            h = min(height[0], height[1])
            return h

        left_p = 0
        right_p = len(height)-1
        max_area = 0

        while left_p < right_p:
            area = min(height[left_p], height[right_p]) * (right_p-left_p)
            if area > max_area:
                max_area = area
            if height[left_p] < height[right_p]:
                left_p += 1
            elif height[left_p] >= height[right_p]:
                right_p -= 1
                
        return max_area

            

