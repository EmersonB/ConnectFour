board = ["."] * 42
player = 'x'

def game_over(board):
    for move in range(0,42):
        if board[move] is not ".":
            if(terminal_state(move) is not None):
                return terminal_state(move)
    return None

def terminal_state(start_move):
    dirs = [1, -1, -7, 7, -8, 8, 6, -6]
    for dir in dirs:
        move = start_move
        current = board[move]
        count = 0
        while move < 42 and move >= 0 and board[move] is current:
            count += 1
            move += dir
            if count is 4:
                return current
    return None


def is_legal(move):
    if board[move] is not '.':
        return False
    return True


def legal_moves():
    return [moves for moves in range(0,7) if is_legal(moves)]


def make_move(move, player):
    if not is_legal(move):
        return False
    column = move
    while (board[column + 7] == "."):
        column += 7
        if column >= 35:
            break

    board[column] = player
    return column

def make_move_local(my_board, move, player):
    column = move
    while (my_board[column + 7] == "."):
        column += 7
        if column >= 35:
            break

    my_board[column] = player
    return my_board


def opponent(player):
    if player == 'x':
        return 'o'
    return 'x'


def display():
    for x in range(len(board)):
        print(board[x], end="")
        if (x + 1) % 7 == 0:
            print(" ")
    print('')

def minimax(player, maxDepth, currentDepth):
    if player == "x":
        return max_dfs(board, player, maxDepth, currentDepth)[1]
    else:
        return min_dfs(board, player, maxDepth, currentDepth)[1]

def max_dfs(board, player, maxDepth, currentDepth):
    if (currentDepth >= maxDepth):
        return 0, None
    if(game_over(board)!= -1):
        if(game_over(board)=="x"):
            return 1000, None
        if (game_over(board) == "o"):
            return -1000, None
        if(game_over(board)=="Draw"):
            return 0, None
    v = -1000
    move = 0
    for m in legal_moves():
        new_value = min_dfs(make_move_local(list(board),m,player), opponent(player), maxDepth, currentDepth + 1)[0]
        if new_value > v:
            v = new_value
            move = m
    return v, move

def min_dfs(board, player, maxDepth, currentDepth):
    if(currentDepth >= maxDepth):
        return 0, None
    if(game_over(board)!= -1):
        if(game_over(board)=="x"):
            return 1000, None
        if (game_over(board) == "o"):
            return -1000, None
        if(game_over(board)=="Draw"):
            return 0, None
    v = 1000
    move = 0
    for m in legal_moves():
        new_value = max_dfs(make_move_local(list(board),m,player), opponent(player), maxDepth, currentDepth + 1)[0]
        if new_value < v:
            v = new_value
            move = m
    return v, move


player = 'x'
display()
move = int(input("move:"))
move = make_move(move, player)
display()
while game_over(board) is None:
#while terminal_state(move) is None:
    #print(move)
    player = opponent(player)
    #move = int(input("move:"))
    move = minimax(player,3,0)
    #while make_move(move,player) is False:
    #    move = int(input("move invalid:"))

    display()
    print('')
print(terminal_state(move)+' wins')
