board = ("---------")
def PlayingField():
    for i in range(len(board)):
        if i == 0 or i == 3 or i == 6:
            print("|", end='')
        if i == 2 or i == 5 or i == 8:
            print(board[i] + "|")
        else:
            print(board[i], end=' ')
PlayingField()
board = list[:8](input("Enter cells: "))
PlayingField()