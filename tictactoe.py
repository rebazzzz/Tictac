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

# Väljer vinnare baserad på deras moves
def Vinnare(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

# Funktionen för spelarens input.
def Spelare():
    run = True
    while run:
        flytta = input("Välj en position att skriva X i mellan ruta 1 till 9\n")
        try:
            # Om man anger en siffra mindre än 0 eller större än 10 så kommer det inte att fungera
            flytta = int(flytta)
            if flytta > 0 and flytta < 10:
                if ledigplats(flytta):
                    run = False
                    skrivbokstaven('X' , flytta)
                
                # Meddelandet för om man väljer en ruta som är tagen.
                else:
                    print('Rutan är inte tomt')
            else:
                print('Ange en siffra 1 till 9')
        # Jag antar att dett aär ett undantag
        except:
            print('Ange en siffra')

# Funktionen för datorns input
def datorn():
    # Detta är möjliga moves för datorn.
    mojligamoves = [x for x , bokstav in enumerate(bord) if bokstav == ' ' and x != 0  ]
    move = 0

    # Det är en for loop, men jag är inte säker på vad det det gör. 
    for let in ['O' , 'X']:
        for i in mojligamoves:
            kopierabordet = bord[:]
            kopierabordet[i] = let
            if Vinnare(kopierabordet, let):
                move = i
                return move

    # Det är en lista med möjöiga rutor man kan välja tror jag.
    kanter = []
    for i in mojligamoves:
        if i in [1 , 3 , 7 , 9]:
            kanter.append(i)

    if len(kanter) > 0:
        move = selectRandom(kanter)
        return move

    if 5 in mojligamoves:
        move = 5
        return move

    edgesOpen = []
    for i in mojligamoves:
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
            Spelare()
            printBord(bord)
        else:
            print("sorry you loose!")
            break

        if not(Vinnare(bord , 'X')):
            move = datorn()
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
