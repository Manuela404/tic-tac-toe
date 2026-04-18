from datetime import datetime
import ast

add = True
looping = True

filename = "savedNotes.txt"
def save(input,filename):
    with open(filename,"w")as f:
        f.write(input)
def loadNotes(filename):
    with open(filename,"r") as f:
        return f.read()

try :
    load = loadNotes(filename)
    noteli = ast.literal_eval(load)
except:
    noteli = []


def addNew(): 
    global noteli
    while True :
        newNote = input("new note : ")
        now = datetime.now()
        addedNotes = f"{now} \n {newNote}"
        noteli.append(addedNotes)
        save(str(noteli),filename)
        print(f"Saved: {addedNotes}")
        continues = input("Do you want add a note?(yes/no)\n")
        if continues.lower() == "no":
            break


def loops():
    global noteli
    try :
        load = loadNotes(filename)
        noteli = ast.literal_eval(load)
        for notes in noteli:
         print(f"\n{notes}")
    except:
        print("There are no current notes.")
        


def settings():
    while True:
        addNote = input("1.Add a new note\n2.Go through all notes\n")
        if addNote == "1":
            addNew()
        if addNote == "2":
            loops()
        
    
settings()