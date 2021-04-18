
"""
1. Get input from the user (at multiple points) 
2. We need to convert some of this input to INTs from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Return a value to a specific index
"""
import random
myList = []
uniqueList = []
#------
'''
    mainProgram()
    Function explanation: this function is where we call all of our functions. 
    Each function has a corresponding number that the user inputs to call it. 
    Call complexity varies; most are the function with brackets after it, but some calls have a logical structure as well. 

'''
def mainProgram(): 
        try: 
            while True:
                print("Hello, there! Let's work with lists!")
                print("Choose from the following options. Type a number below!")
                choice = input("1. Add to a list, 2. Return the value at an index position! 3: Random Int 4: Add a bunch, 5: Print list, 6: Linear Search, 7: Sort List, 8: Print Lists 9: Recursive Binary Search, 10: Iterative Binary Search, 11: Remove Numbers, 12: Clear List, 13: Quit Program  ")
                if choice == "1": 
                    addToList()
                elif choice == "2": 
                    indexValues()
                elif choice == "3":
                    randomSearch()
                elif choice == "4": 
                    addABunch()
                elif choice == "5":
                    print (myList)
                elif choice == "6":
                    linearSearch()
                elif choice == "7":
                    sortList(myList)
                elif choice == "8":
                    printLists()
                elif choice == "9":
                    binSearch = input('What number are you looking for?  ')

                    result = recursiveBinarySearch(uniqueList, 0, len(uniqueList)-1, int(binSearch))

                elif choice == "10": 
                    binSearch = input('What number are you looking for?  ')
                    result = iterativeBinarySearch(uniqueList, int(binSearch))
                    if result !=-1:
                        print(f'Your number is at index position {result}') 
                    else:
                        print('Your number is not found in that list, bud!')


                elif choice == "11":
                    removeNumber()
                elif choice == "12":
                    clearList()
                elif choice == "13":
                    break
        except: 
                print ("You made a whoopsie!")
#------
'''

    addToList()
    Function explanation: this function allows us to add single numbers to the list myList().
    This function works by using the list.append(object) method to add a single integer to the myList() via an input. 
'''
def addToList(): 
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
#------
'''
    addABunch()
    Function explanation: This function allows us to add multiple random integers to the list. 
    By using two inputs, a for x in range statement, and another list.append(object) method, we are able to add a specified amount of random integers to the list.   
'''
def addABunch(): 
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("How many new integers would you like to add?   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range (0, int(numToAdd)):
        myList.append(random.randint(0,int(numRange))) 
    print("Your list is now complete.")
#------
'''
    indexValues()
    Function explanation: this function finds a number at a specified index position by using the list(int) method, which automatically does what list.index is normally used for: finding an index position in a list. 
    Furthermore, we use an input to define the integer that the user wants, and an int method since inputs output strings. 
'''
def indexValues(): 
    print("Ohhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?  ")
    print (myList[int(indexPos)])
#------
'''
    sortList()
    Function explanation: this function takes all the values in myList() and sorts them from lowest value to highest value into a seperate list: uniqueList(). 
    In detail, sortList() uses a for x in (object) method, with x representing all the numbers in myList(). These numbers are then sorted using the list.sort() method, after this, we use an input to show the user their sorted list.  
'''
def sortList(myList):
    print ("A little birde told me you need some sorted data")
    for x in myList: 
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort() 
    showMe = input("Wanna see your new list? Y/N   ")
    if showMe.lower() == "y":
        print(uniqueList) 
#------
'''
    randomSearch()
    Function explanation: this function performs a random search of the list by using a random number generated within the length of the list.
'''
def randomSearch(): 
        print("rAnDoM sEaRcH?")
        print(myList[random.randint(0, len(myList)-1)])
#------
'''
    linearSearch()
    Function explanation: this function sorts through every number in the list to find a single number
    In detail, we use an input to get the desired number, then use a for x in range statement to search the length of myList() for that number. 
'''
def linearSearch(): 
    print("We're gonna check out each item one at a time in your list! This sucks.")
    searchItem = input("What you lookin for, pardner?     ")
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            print(f"Your item is at index position {x}")
    else: 
        print("This number is not in my list")
#------
'''
    recursiveBinarySearch()
    Function Explanation: recursiveBinarySearch uses an algorithm (aka dark magic) to search the list in two sections at once until a midpoint is reached. 
    In detail, this function searches between a high and low point with a midpoint that is established by dividing between these two points. The endpoints are decreased or increased until both reach the same midpoint. This is done via recursion. 
'''
def recursiveBinarySearch(uniqueList, low, high, x):
    if high>= low: 
        mid = (high+low)//2
        if uniqueList[mid] == x: 
            print(f'your number is at index position {mid}')
            return mid 
        elif uniqueList[mid]>x: 
            return recursiveBinarySearch (uniqueList, low, mid-1, x)
        else: 
            return recursiveBinarySearch(uniqueList, mid+1, high, x)

    else: 
        print("Your number isn't here!")
#------
'''
    iterativeBinarySearch()
    Function explanation: this function works quite similarly to recursiveBinarySearch, however, it uses iteration (the process of going through something until outcome is achieved) to sort through the list in a binary manner. 
'''
def iterativeBinarySearch(uniqueList, x): 
    low = 0
    high = len(uniqueList)-1
    mid = 0 

    while low <= high: 
        mid = (high+low)//2

        if uniqueList[mid]<x: 
            low = mid + 1 

        elif uniqueList[mid]>x: 
            high = mid-1
        else: 
            return mid 
    return -1
#------
'''
    removeNumber()
    Function explanation: removeNumber uses a modified linear search method to sort through the list, but performs a list.pop(object) method to remove the specified number at the end of the function. 
    In detail, this function uses a while method to find the index position of the specified number, along with an int method (inputs output strings!). 
'''
def removeNumber():
        print("We're gonna remove some numbers here!") 

        removeItem = input("What number do you want to remove?     ")
        removeItem = int(removeItem)
        
        while removeItem in myList:
            position = myList.index(int(removeItem))
            myList.pop(position)
        print ("The requested numbers have been removed!  ")
#------
'''
    clearList()
    Function explanation: clearList uses an if/else conditional to determine if the user wants to clear the list (the list clearing itself is just done with a list.clear(object) method), with a 'y' input yielding a cleared list. 
'''
def clearList(): 
    clear = input ("Are you sure you want to clear the list? Y/N    ")
    if clear.lower() == "y":
        list.clear(myList)
        print ("The list has been cleared!")
    else:
        print ("Action Canceled")
#------
'''
printLists()
Function explanation: printLists uses an if/else conditional to determine if uniqueList() is full; if it is, we use another if/else conditional to ask the user which list they want to see. A 'sorted' response will yield uniqueList(), while an 'unsorted' response will yield myList().
'''        
def printLists():   
    if len(uniqueList) == 0: 
        print(myList)
    else:
        whichOne = input("Which list? sorted or unsorted     ")
        if whichOne.lower() == "sorted":
            print(uniqueList)
        else:
            print(myList)
if __name__ == "__main__": 
    mainProgram()