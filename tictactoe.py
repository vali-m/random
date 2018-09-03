# Below function probably only works in Jupyter Notebook
# from IPython.display import clear_output


play_sym = ['x', 'O', ' ']

def start():
    print("Welcome to Tic Tac Toe.")
    sel = input("to begin, do you want to be X or O?")
    if 'x' == sel or sel == 'X':
        return 1
    elif 'o' == sel or 'O'== sel:
            return 2
    else:
        return start()


def check_win():
    global board
    if (hasWin([1,2,3])
        or hasWin([4,5,6])
        or hasWin([7,8,9])
        or hasWin([1,4,7])
        or hasWin([2,5,8])
        or hasWin([3,6,9])
        or hasWin([1,5,9])
        or hasWin([3,5,7])):
        return True
    return False

# deprecated
def getSum(lst):
    sum = 0
    for i in lst:
       sum += i
#     print('Sum = {}'.format(sum))
    return sum

def hasWin(indexList):
    global board
    valList = [board[x - 1] for x in indexList] # A wild List Comprehension
    return (valList[0] != -1 and valList[1] == valList[0] == valList[2])
    sum = getSum(valList)
    return (sum == 3 or sum == 6)

def getNextPlayer(crtPlayer):
    if crtPlayer == 1:
        return 2
    else:
        return 1
    
def printBoard():
    global board
    print("{}|{}|{}".format(getSymbol(1),getSymbol(2),getSymbol(3)))
    print("-----")
    print("{}|{}|{}".format(getSymbol(4),getSymbol(5),getSymbol(6)))
    print("-----")
    print("{}|{}|{}".format(getSymbol(7),getSymbol(8),getSymbol(9)))

def getSymbol(fakeIndex):
    global board
    val = board[fakeIndex - 1]
    if val == -1:
        return ' '
    elif val == 1:
        return 'X'
    else:
        return 'O'
    
def play():
    global board
    board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    crtPlayer = start()
    round = 0
    while True:
        printBoard()
        in1 = input(f"[{round}]Player {crtPlayer} SELECT field (1-9)")
        if not in1.isnumeric:
            print("Please enter a number between 1 and 9")
            in1 = input(f"[{round}]Player {crtPlayer} SELECT field (1-9)")
            if not in1.isnumeric:
                break
        field = int(in1) - 1
        if (field not in range(0,9) or board[field] != -1):
            print("INVALID MOVE!! PLEASE TRY AGAIN")
            continue
        board[field] = crtPlayer
        round += 1
        if check_win():
        #    clear_output()
            printBoard()
            print(f"Player {crtPlayer} has won on turn {round}")
            return
        crtPlayer = getNextPlayer(crtPlayer)
    #    clear_output()