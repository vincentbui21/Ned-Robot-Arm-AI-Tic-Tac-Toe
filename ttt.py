from opencv import detect_move

board = [ 
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]

#the board variable (2D list) now represents as the tic-tac-toe board.
#let's all agree: 0_none ; 1_o exist (player); -1_x exist(AI) 

a, b=detect_move()
board[a][b] = "o"
print(board[a][b])