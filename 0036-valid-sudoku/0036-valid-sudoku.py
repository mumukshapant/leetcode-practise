class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowset=set() 
        colset= set()
        boxset= set()

        for r in range(9): 
            for c in range(9): 
                value = board[r][c]

                # Ignore empty cells
                if value == ".":
                    continue

                if (value,r) in rowset or (value,c) in colset: 
                    return False
                boxnumber = (r//3)*3+(c//3)
                if (value, boxnumber) in boxset:
                    return False
                rowset.add((value,r))
                colset.add((value,c))
                boxset.add((board[r][c], boxnumber))
        return True

        
                
