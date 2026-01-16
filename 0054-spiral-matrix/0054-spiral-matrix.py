class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return
        output = []
        rows, cols = len(matrix), len(matrix[0])   # to check oob
        x, y, dx, dy = 0, 0, 1, 0   # we want to first move right
        for _ in range(rows*cols): #ensure we stop
            output.append(matrix[y][x])
            matrix[y][x] = "."
        
            if not 0<= x+dx < cols or not 0<=y+dy<rows or matrix[y+dy][x+dx] == ".":
                dx, dy = -dy, dx
            
            x += dx
            y += dy            
        
        return output