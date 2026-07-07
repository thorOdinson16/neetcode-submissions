class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            x = set()
            y = set()
            z = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in x:
                    return False
                else:
                    x.add(board[i][j])
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in y:
                    return False
                else:
                    y.add(board[j][i])
        for j in range(0,9,3):
            for k in range(0,9,3):
                a = set()
                for l in range(j,j+3):
                    for m in range(k,k+3):
                        if board[l][m] == '.':
                            continue
                        elif board[l][m] in a:
                            return False
                        else:
                            a.add(board[l][m])                           
        return True