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
            
#Function your user move
def move():
    notlegit = True
    while notlegit:
        place = int(input("Choose the position for your move (1-9): "))
        if spaces[place-1] == " ":
            spaces[place-1] = player
           
            notlegit = False

def score(position,scoreO,scoreX):
    if spaces[position] == "X":
        scoreX+=1
        print(f"X: {scoreX}\nO: {scoreO}")
    else:
        scoreO += 1 
        print(f"X: {scoreX}\nO: {scoreO}")
    scoresData['X'] = scoreX
    scoresData['o'] = scoreO
    savefile(str(scoresData),filename)
game = True

def check_win(position1,position2,position3):
      if  spaces[position1] != " " and spaces[position1] == spaces[position2] and spaces[position1] == spaces[position3]:
            print(f"Player {spaces[position1]} won!")
            score(0,scoreO,scoreX)
            game = False
            return game

def play():                  
    while game:
        move()
        if " " not in spaces :
            print("It was a tie!!!")
            break
        else :
            computerMove()
            drawBoard()
             #checks for horizontal win
            check_win(0,1,2)
            check_win(3,4,5)
            check_win(6,7,8)  
            #checks for vertical win
            check_win(0,3,6)
            check_win(1,4,7)        
            check_win(2,5,8)  
            #checks for across win
            check_win(0,4,8)    
            check_win(2,4,6)    
 
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
