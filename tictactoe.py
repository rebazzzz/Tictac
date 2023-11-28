# Printar 9 rutor
bord = [' ' for x in range(10)]

# Det är funktionen för X och O bokstäverna
def skrivbokstaven(bokstav,pos):
    bord[pos] = bokstav

# Är de tomma rutorna på bordet som man kan skriva en bokstav i
def ledigplats(pos):
    return bord[pos] == ' '

# Det printar själva bordet som man spelar på
def printBord(bord):
    print('   |   |   ')
    print(' ' + bord[1] + ' | ' + bord[2] + ' | ' + bord[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bord[4] + ' | ' + bord[5] + ' | ' + bord[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bord[7] + ' | ' + bord[8] + ' | ' + bord[9])
    print('   |   |   ')

# Kontrollerar om det finns tomma rutor. Om det är finns plats så fortsätter spelet annars avbryts det.
def eBordetFull(bord):
    if bord.count(' ') > 1:
        return False
    else:
        return True

def Vinnare(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9\n")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if ledigplats(move):
                    run = False
                    skrivbokstaven('X' , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')

        except:
            print('Please type a number')

def computerMove():
    possibleMoves = [x for x , bokstav in enumerate(bord) if bokstav == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = bord[:]
            boardcopy[i] = let
            if Vinnare(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game!")
    printBord(bord)

    while not(eBordetFull(bord)):
        if not(Vinnare(bord , 'O')):
            playerMove()
            printBord(bord)
        else:
            print("sorry you loose!")
            break

        if not(Vinnare(bord , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                skrivbokstaven('O' , move)
                print('computer placed an o on position' , move , ':')
                printBord(bord)
        else:
            print("you win!")
            break




    if eBordetFull(bord):
        print("Tie game")

while True:
    x = input("Do you want to play? Press y for yes or n for no (y/n)\n")
    if x.lower() == 'y':
        bord = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
