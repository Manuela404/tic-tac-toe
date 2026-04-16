import random
import ast

print("Welcome to tic tac toe !!")
print('You are "X"')

spaces =[" "]*9
player = "X"
computer = "O"
scoreX = 0 
scoreO = 0 
filename = "leaderboard.txt"

def savefile(input,filename):
    with open(filename,"w") as f:
        f.write(input)
def loadFile(filename):
    with open(filename,"r") as f:
        return f.read()
try :
    loadedData = loadFile(filename)
    scoresData = ast.literal_eval(loadedData)
except:
    print("There are no current scoreboard data")
    scoresData = {}

def drawBoard():        
    board =  f"  {spaces[0]}       |   {spaces[1]}       |   {spaces[2]}       \n__________|___________|___________\n  {spaces[3]}       |   {spaces[4]}       |   {spaces[5]}       \n__________|___________|___________\n  {spaces[6]}       |   {spaces[7]}       |   {spaces[8]}       \n"
    print(board)

def computerMove():
    compvalid = True
    while compvalid:
        compMove = random.randint(0,8)
        if spaces[compMove] == " ":
           spaces[compMove] = computer
           compvalid = False
            

def move():
    notlegit = True
    while notlegit:
        place = int(input("Choose the position for your move (1-9): "))
        if spaces[place-1] == " ":
            spaces[place-1] = player
           
            notlegit = False

def score(position):
    global scoreO
    global scoreX
    if spaces[position] == "X":
        scoreX+=1
        print(f"X: {scoreX}\nO: {scoreO}")
    else:
        scoreO += 1 
        print(f"X: {scoreX}\nO: {scoreO}")
    scoresData['X'] = scoreX
    scoresData['o'] = scoreO
    savefile(str(scoresData),filename)

def play():         
    game = True         
    while game:
        move()
        if " " not in spaces :
            print("It was a tie!!!")
            break
        else :
            computerMove()
            drawBoard()
        if  spaces[0] != " " and spaces[0] == spaces[1] and spaces[1] == spaces[2]:
            print(f"Player {spaces[0]} won!")
            score(0)
            game = False
        elif spaces[3] != " " and spaces[3] == spaces[4] and spaces[4] == spaces[5]:
            print(f"Player {spaces[5]} won!")
            score(5)
            game = False
        elif spaces[6] != " " and spaces[6] == spaces[7] and spaces[7] == spaces[8]:
            print(f"Player {spaces[8]} won!")
            score(8)
            game = False
        elif spaces[0] != " " and spaces[0] == spaces[3] and spaces[3] == spaces[6]:
            print(f"Player {spaces[6]} won!")
            score(6)
            game = False
        elif spaces[1] != " " and spaces[1] == spaces[4] and spaces[4] == spaces[7]:
            print(f"Player {spaces[7]} won!")
            score(7)
            game = False
        elif spaces[2] != " " and spaces[2] == spaces[5] and spaces[5] == spaces[8]:
            print(f"Player {spaces[8]} won!")
            score(8)
            game = False
        elif spaces[0] != " " and spaces[0] == spaces[4] and spaces[8] == spaces[4]:
            print(f"Player {spaces[8]} won!")
            score(8)
            game = False
        elif spaces[2] != " " and spaces[2] == spaces[4] and spaces[4] == spaces[6]:
            print(f"Player {spaces[6]} won!")
            score(8)
            game = False
    
def main():
    while True:
        choice = input('1.Play game\n2.Check scoreboard\n3.Exist game\n')
        if int(choice) == 1:
            global spaces
            spaces = [" "]* 9
            play()
        elif int(choice) == 2:
            try :
                loadedData = loadFile(filename)
                scoresData = ast.literal_eval(loadedData)
                print("_____leaderboard_______")
                for player,score in scoresData.items():
                    print(f"{player} : {score}")
            except:
                print("There are no current scoreboard data")
                scoresData = {}
        else :
             break
main()