class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create hasmaps for each column, row and square
        cols = collections.defaultdict(set) 
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9): # nested forloop to brute force iterate through entire sudoku

                if board[r][c] == ".": # "." - empty -> ignore
                    continue

                # if duplicate - found in all the collections -> return False
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[r] or
                    board[r][c] in squares[(r//3, c//3)]): # rounded down always -> return correct 3x3 square
                    return False

                # add if unique to all collections at once
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
            
        return True # returns True if iteration through whole sudoku is complete