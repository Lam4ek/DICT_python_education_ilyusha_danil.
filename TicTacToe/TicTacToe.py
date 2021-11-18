symbols = list("---------")
def PlayingField():
    for i in range(len(symbols)):
        if i == 0 or i == 3 or i == 6:
            print("|", end='')
        if i == 2 or i == 5 or i == 8:
            print(symbols[i] + "|")
        else:
            print(symbols[i], end=' ')
PlayingField()
def check_result(symbols):
    win_coord = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for each in win_coord:
        if symbols[each[0]] == symbols[each[1]] == symbols[each[2] != '-']:
            print(str(symbols[each[0]]) + " win" )
            break

if __name__ == "__main__":
    symbols = list(input("Enter cells: "))
    PlayingField()
    check_result(symbols)