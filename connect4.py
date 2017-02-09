
board = [-1] * 48
player = 'x'

def terminal_state():
    dirs = [1,-1,-7,7,-8,8,6,-6]
    for move in range(0,48):
        for dirt in dirs:
            current = board[move]
            count = 0
            while move <= 42 and move >= 0 and board[move] is not -1 and board[move] is current:
                count+=1
                move += dirt
                if count is 4:
                    return current
    return None
        
        
def is_legal(move):
    if move < 0 or move > 48:
        return False
    if board[move] != -1:
        return False
    if move <= 34:
        if board[move+7] == -1:
            return False
    if move % 7 == 0: #border
        return False
    return True
        
def legal_moves():
    return [moves for moves in board if is_legal(move)]


def make_move(move, player):
    if is_legal(move):
        board[move] = player
    else:
        return False
    
def opponent(player):
    if player == 'x':
        return 'o'
    return 'x'
def display():
    for x in range(6):
        for y in range(8):
            print(board[x*y],end="")
        print(" ")
        
player = 'x'
display()
print(terminal_state())
while terminal_state() is None:
    move = int(input("move:"))
    while make_move(move, player) == False:
        move = int(input("Invalid Move, New Move:"))
    print(board)
    player = opponent(player)
