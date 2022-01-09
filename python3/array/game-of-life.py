"""game-of-life
289. Game of Life
Medium

3420

381

Add to List

Share
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 


"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        #print (m, n) 
        board1 = [0]*m
        for i in range(m):
            board1[i] = [0]*n
            
        for i in range(m):
            print("I:", i)
            for j in range(n):              
                #print(board[i][j])
                state = board[i][j]
                neibs = 0
                #1-2
                if i-1 >= 0 and j-1 >= 0: neibs += board[i-1][j-1]; print(i,j,"^\ ",board[i][j] ,"_ ", board[i-1][j-1], neibs)
                if i-1 >= 0 : neibs += board[i-1][j]; print(i,j,"^| ",board[i][j] ,"_ ", board[i-1][j], neibs) 
                
                #3-4
                if i-1 >= 0 and j+1 < n: neibs += board[i-1][j+1]; print(i,j,"/^ ",board[i][j] ,"_ ", board[i-1][j+1]) 
                if j+1 < n : neibs += board[i][j+1]; print(i,j,"-> ",board[i][j] ,"_ ", board[i][j+1], "*") 
                
                #5-6
                if i+1 < m and j+1 < n: neibs += board[i+1][j+1]; print(i,j,"\. ",board[i][j] ,"_ ", board[i+1][j+1]) 
                if i+1 < m : neibs += board[i+1][j]; print(i,j,"|. ",board[i][j] ,"_ ", board[i+1][j]) 
                
                #7-8
                if i+1 <m and j-1 >= 0: neibs += board[i+1][j-1]; print(i,j,"./ ",board[i][j] ,"_ ", board[i+1][j-1]) 
                if j-1 >= 0 : neibs += board[i][j-1]; print(i,j,"<- ",board[i][j] ,"_ ", board[i][j-1], neibs) 
                
                if state == 1 and neibs < 2 : board1[i][j] = 0
                if state == 1 and (neibs == 3 or neibs == 2): board1[i][j] = 1
                if state == 1 and neibs > 3: board1[i][j] = 0
                if state == 0 and neibs == 3: board1[i][j] = 1
                
#        print(board1) 
        for i in range(m):
            for j in range(n):              
                board[i][j] = board1[i][j]                               
                    
"""  
1. Любая живая клетка с менее чем двумя живыми соседями умирает, как если бы это было вызвано недостаточным населением.
(1)  x < 2  Умирает  (0)

2. Любая живая клетка с двумя-тремя живыми соседями живет до следующего поколения.
(1)  x = 2 or x = 3  Живёт  (1)  

3. Любая живая клетка с более чем тремя живыми соседями умирает, как бы от перенаселения.
(1)   x > 3  Умирает (0)

4. Любая мертвая клетка, имеющая ровно три живых соседа, становится живой клеткой, как бы путем размножения.

        for i in range(m): 
            for j in range(n): 
                board1 [i][j] = 0
"""