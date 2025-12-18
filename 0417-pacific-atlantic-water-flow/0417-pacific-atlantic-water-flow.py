class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights:
            return []
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean, heights):
            rows, cols = len(heights), len(heights[0])
            if (r, c) in ocean:
                return
            ocean.add((r, c))

            for dr, dc in DIRECTIONS:
                if r + dr >= 0 and r + dr < rows and c + dc >= 0 and c + dc < cols:
                    if heights[r+ dr][c+ dc] >= heights[r][c]:
                        dfs(r+dr, c+dc, ocean, heights)
        
        #do dfs for top row + left col -> pacific
        for c in range(len(heights[0])):
            dfs(0, c, pacific, heights) # top row
            dfs(len(heights)-1, c, atlantic, heights) # bottom row
        for r in range(len(heights)):
            dfs(r, 0, pacific, heights) # left col
            dfs(r, len(heights[0])-1, atlantic, heights) #right col
        
        return list(pacific & atlantic)

            



        