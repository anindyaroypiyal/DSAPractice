from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    a = []

    r = 0
    c = 0

    elems = nRows * mCols
    
    while(len(a) != elems):
        for j in range(mCols):
            if (mat[r][j] not in a):
                a.append(mat[r][j])
                # print([mat[r][j]])
                c = j
                
        for i in range(nRows):
            if (mat[i][c] not in a):
                a.append(mat[i][c])
                # print([mat[i][c]])
                r = i

        for j in range(c, -1, -1):
            if (mat[r][j] not in a):
                a.append(mat[r][j])
                # print([mat[r][j]])
                c = j

        for i in range(r, -1, -1):
            if (mat[i][c] not in a):
                a.append(mat[i][c])
                # print([mat[i][c]])
                r = i
        mCols -= 1
        nRows -= 1

    for i in a:
        print(i, end=' ')



























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1