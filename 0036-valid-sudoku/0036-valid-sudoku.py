class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                val = board[i][j]
                if val == ".":
                    pass
                else:
                    box_index = (i // 3) * 3 + (j // 3)
                    if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                        return False
                    else:
                        rows[i].add(val)
                        cols[j].add(val)
                        boxes[box_index].add(val)
        
        return True
                    
                

        