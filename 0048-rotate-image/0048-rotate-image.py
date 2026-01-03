class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # want to transpose and then reverse bc doing all in place in two for loops will replace the elements that are already swapped
        #want to transpose first and then reverse the rows
        n = len(matrix)

        #transpose
        for r in range(n):
            for c in range(r, n):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp
    
        for r in range(n):
            matrix[r].reverse() #.reverse() returns null
        
        return matrix
        