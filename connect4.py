board = ["."] * 42
player = 'x'


def terminal_state(move):
    dirs = [1, -1, -7, 7, -8, 8, 6, -6]
    for dir in dirs:
        current = board[move]
        count = 0
        while move <= 42 and move >= 0 and board[move] is current:
            count += 1
            move += dir
            if count is 4:
                return current
    return None


def is_legal(move):
    if move < 0 or move > 41:
        return False
    if board[move] != -1:
        return False
    if move <= 34:
        if board[move + 7] == -1:
            return False
    if move % 7 == 0:  # border
        return False
    return True


def legal_moves():
    return [moves for moves in board if is_legal(move)]


def make_move(move, player):
    column = move
    while (board[column + 7] == "."):
        column += 7
        if column >= 35:
            break

    board[column] = player
    return column


def opponent(player):
    if player == 'x':
        return 'o'
    return 'x '


def display():
    for x in range(len(board)):
        print(board[x], end="")
        if (x + 1) % 7 == 0:
            print(" ")


player = 'x'
display()
move = int(input("move:"))
move = make_move(move, player)
display()
while terminal_state(move) is None:
    player = opponent(player)
    move = int(input("move:"))
    while make_move(move, player) == False:
        move = int(input("Invalid Move, New Move:"))
    display()
