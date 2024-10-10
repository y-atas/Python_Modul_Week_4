import membersTransactions
import bookTransactions
import json
import menuDisplay as display
import os

emtySpot= "emtySpot.json"
membersFileName= "members.json"

members =[]
semty_slot=[]


def saveData(file,data):
   
    if os.path.exists(file):
        with open(file,"r", encoding="utf-8") as file:
            json.dump(data,file,indent=4)
    else:
        with open(file, "w+", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

while True:
    display.displayMainMenu()
    choose = int(input("Enter your preference (1 to 3 ):"))
    
    match choose :

        case 1:
            print("\n\033[95mIt is MEMBERS transaction appear.\n")
            while True :
                display.displaymembersMenu()
                choose_mem_transaction = int(input("Enter your preference (0 to 7 ):"))
                match choose_mem_transaction:
                    case 0:
                        break
                    
        case 2 :
            print("\n\033[91mIt is BOOK transaction appear.\n")
            while True:

                display.displayBookMenu()
                choose_book_transaction = int(input("Enter your preference (0 to 4 ):"))
                match choose_book_transaction:
                    case 0:
                        break


        case 3:
            print("\033[95mYou are exit(3) ")
            break
        
        

