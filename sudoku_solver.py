class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # self.result = []

        unkPos = []
        self.rowSet, self.colSet, self.boxSet = [set() for i in range(9)], [set() for i in range(9)], [[set() for i in range(3)] for j in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    unkPos.append((i, j))
                else:
                    self.rowSet[i].add(board[i][j])
                    self.colSet[j].add(board[i][j])

                    self.boxSet[i//3][j//3].add(board[i][j])

        self.backtrack(board, unkPos, 0, len(unkPos))
        

    def backtrack(self, board, unkPos, left, n):
        if left == n:            
            return True

        i, j = unkPos[left]

        for num in range(1, 10):
            if (str(num) not in self.rowSet[i]) and (str(num) not in self.colSet[j]) and (str(num) not in self.boxSet[i//3][j//3]):
                board[i][j] = str(num)

                self.rowSet[i].add(str(num))
                self.colSet[j].add(str(num))
                self.boxSet[i//3][j//3].add(str(num))

                res = self.backtrack(board, unkPos, left+1, n)
                
                if res:
                    return board

                board[i][j] = "."

                self.rowSet[i].remove(str(num))
                self.colSet[j].remove(str(num))
                self.boxSet[i//3][j//3].remove(str(num))
