def checkIsSafe(board,row,col):
    r = row-1
    c = col
    #checking for straight up
    while r >= 0:
        if board[r][c] == "1":
            return False
        r -= 1
    
    r = row-1
    c = col-1
    #checking for left diagonal
    while r >= 0 and c >= 0:
        if board[r][c] == "1":
            return False
        r -= 1
        c -= 1
    
    r = row-1
    c = col+1
    #chekcing for right diagonal
    while r >= 0 and c < len(board[0]):
        if board[r][c] == "1":
            return False
        r -= 1
        c += 1
    
    return True

def makeBoard(board):
    new = []
    for i in range(len(board)):
        string = ""
        for j in range(len(board[i])):
            string += board[i][j]
        new.append(string)
    return new

def backtrack(board,queens,row=0,col=0):
    if queens == 0:
        ans = makeBoard(board)
        return [ans]
    else:
        output = []
        for i in range(len(board[0])):
            if checkIsSafe(board,row,i):
                board[row][i] = "1"
                output += backtrack(board,queens-1,row+1,0)
                board[row][i] = "0"
    return output


def solveNQueens(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append("0")
    ans = backtrack(board,n)
    k = []
    for i in ans:
        c = []
        for j in i:
            for p in j:
                c.append(p)
        k.append(c)
    return k
