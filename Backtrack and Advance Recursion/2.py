def solveNQueens(n):
    # Write your code here.
    col = set()
    posDiag = set()
    negDiag = set()
    res = []

    board = [["0"]*n for i in range(n)]
    
    def backtrack(r):
        if r == n:
            c = [' '.join(row) for row in board]
            res.append(c)
            return
        
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:  #on the positive diagonal any (r+c) would be same, and on the negative diagonal (r-c) will be same.
                continue
            
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "1"

            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "0"
    
    backtrack(0)
    return res
