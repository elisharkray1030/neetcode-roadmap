class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) 
        # ROWS - horizontal -> len(matrix) number of arrays 
        # COLS - vertical -> len(matrix[0]) number of elements in subarray[0]

        top, bot = 0, ROWS - 1
        # top = 0
        # bot = ROWS -1 -> last row

        while top <= bot: # binary search row

            row = (top + bot) // 2 # set row - midpoint

            if target > matrix[row][-1]: # target is larger than largest value on row
                top = row + 1 # row + 1 -> go to the next row
            
            elif target < matrix[row][0]: # target is smaller than 
                bot = row - 1 # row - 1 -> go to previous row

            else: # target is within range 
                break
                
        if not (top <= bot): 
            return False


        row = (top + bot) // 2 # using top and bot - initialize row
        l, r = 0, COLS -1 
        # l = 0 -> left most element
        # r = COLS -1 -> right most element (no. of columns - 1)

    
        while l <= r: # binary search on the row
        
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False