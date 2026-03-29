class Solution(object):
    def solveNQueens(self, n):
        
        # Each Q can be in one row 
        # Each Q can be in one col 

        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        res=[]
        if n == 1:
            return [["Q"]]

        if n==2 or n==3 : 
            return []
        board = [["."]*n for _ in range(n)]
        
        used_col = set() 
        used_diag=set() 
        used_opp_diag= set()

        def backtrack(row): 
            if row==n :
                curr_row = ["".join(r) for r in board]
                res.append(curr_row) 
                return

            for col in range(n):
                diag = row-col 
                opp_diag = row+col 

                if col in used_col or diag in used_diag or opp_diag in used_opp_diag: 
                    continue 
                board[row][col]="Q"

                # Mark visited 
                used_col.add(col)
                used_diag.add(diag)
                used_opp_diag.add(opp_diag)

                backtrack(row+1)


                board[row][col] = "."
                used_col.remove(col)
                used_diag.remove(diag)
                used_opp_diag.remove(opp_diag)

        backtrack(0)
        return res 
