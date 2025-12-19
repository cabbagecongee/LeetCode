class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic, pacific = set(), set()
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(heights), len(heights[0])
        def bfs(r, c, heights, ocean):
            if (r, c) in ocean:
                return
            ocean.add((r,c))
            for dr, dc in DIRECTIONS:
                row = dr + r
                col = dc + c
                if 0 <= row < rows and 0 <= col < cols:
                    if heights[r][c] <= heights[row][col]:
                        bfs(row, col, heights, ocean)
            return
        
        # pacific -> top row, atlantic -> bottom row
        for i in range(cols):
            bfs(0, i, heights, pacific)
            bfs(rows-1, i, heights, atlantic)
        
        #pacific -> left col, atlantic -> right col
        for j in range(rows):
            bfs(j, 0, heights, pacific)
            bfs(j, cols-1, heights, atlantic)
        
        return list(atlantic & pacific)

        