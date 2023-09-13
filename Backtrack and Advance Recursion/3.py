import collections
def isItSudoku(matrix):

    # Write your code here.
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) #key = (r//3,c//3) integer division, main trick


    for r in range(9):
        for c in range(9):

            if matrix[r][c] == 0:
                continue
                
            if (matrix[r][c] in rows[r]) or (matrix[r][c] in cols[c]) or (matrix[r][c] in squares[(r // 3, c // 3)]):
                return False
            
            cols[c].add(matrix[r][c])
            rows[r].add(matrix[r][c])
            squares[(r // 3, c // 3)].add(matrix[r][c])
    return True