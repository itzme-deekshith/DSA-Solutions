class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            col = []
            for j in range(9):
                x= board[j][i]
                if x != '.' and x not in col:
                    col.append(board[j][i])
                elif x in col:
                    return False

        for row in board:
            x = []
            for j in row:
                if j != '.':
                    x.append(j)
            if len(x) != len(set(x)):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                b = []
                for x in range(i,i+3):
                    b.append([board[x][j],board[x][j+1],board[x][j+2]])
                res =[]
                for l in b:
                    for m in l:
                        if m != '.':
                            res.append(m)

                if len(res) != len(set(res)):
                    return False
        
        return True
    
Obj = Solution()
board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
res = Obj.isValidSudoku(board)
for i in board:
    print(i)
print("Is valid sudoku --> ", res)