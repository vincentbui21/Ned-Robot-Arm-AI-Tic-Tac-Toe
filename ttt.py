from opencv import detect_move


board = [ 
        ' ', ' ',' ',
        ' ', ' ',' ',
        ' ', ' ',' '
        ]


a=detect_move()
board[a] = "o"
print(board[a])

