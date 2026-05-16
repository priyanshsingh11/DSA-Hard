class Solution(object):
    def exist(self, board, word):
        m=len(board)
        n=len(board[0])

        def travel(i,j,k):
            if k==len(word): return True

            if (i<0 or j<0 or i>=m or j>=n): return False

            if (board[i][j]!=word[k]): return False
            
            temp=board[i][j]
            board[i][j]="#"

            founding=(travel(i+1, j, k+1) or
                travel(i-1, j, k+1) or
                travel(i, j+1, k+1) or
                travel(i, j-1, k+1)
            )
            board[i][j]=temp
            return founding

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and travel(i,j,0): return True

        return False
