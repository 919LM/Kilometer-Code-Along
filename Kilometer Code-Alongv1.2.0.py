"""
1. Get input from the user (at multiple points) 
2. We need to convert some of this input to INTs from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Return a value to a specific index
"""
import random
myList = []
def mainProgram(): 
    while True:
        try: 
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("1. Add to a list, 2. Return the value at an index position! 3: Quit    ")
            if choice == "1": 
                addToList()
            elif choice == "2": 
                indexValues()
            elif choice == "3":
                break
        except: 
                print ("You made a whoopsie!")
    #TO ADD: 1. A way to loop the action, 
    # 2. A way to quit, 3. Exit Program
def addToList(): 
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

def indexValues(): 
    print("Ohhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?  ")
    print (myList[int(indexPos)])
def randomSearch(): 
        print("rAnDoM sEaRcH?")
        print(myList[random.randint(0, len(myList)-1)])
if __name__ == "__main__": 


    mainProgram()