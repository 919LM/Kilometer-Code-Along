README FILE

Section 1: Software Instructions: 
First off, you'll need to run the program. Do this by pressing F5, and a prompt will pop up.
There are a series of choices regarding which program to run; as the user, you must start with either option "1" (Add to List) or option "4" (Add a Bunch). 
To use Add to List, enter the number "1" in the terminal. Add the integer (a number with no decimal places) you want into the prompt that appears in the terminal.
The first option allows you to add single integers to the list, while the second option allows you to add multiple randomly generated integers to the list.
Once the desired integers are added, there are a number of different routes you can take. If you would like to perform any form of search other than the random search, input "7" to sort the list. 


UNSORTED OPTIONS: 

"1": Add to List. Add one user-specified integer to the list. Input the integer you want to add to the list. 
"2": Index Values. This allows the user to find an integer at a specified index position in the list. Enter the index position into the terminal, and the program will produce the integer. 
"3": Random Search. Have the computer find an integer for you. Just press 3! 
"4": Add a Bunch. Specify the number and range of integers, then have the computer do the rest!	Enter the desired range and amount of integers when prompted to use this function.
"5": Print List. Prints the list myList(). No actions other than pressing "5" to begin the function on this one. 
"11": Remove Number. Removes a number or set of numbers specified by the user. Specify the integer you would like to remove when prompted.  
"12": Clear list. Simply press "y" to clear all the integers! 
"13": Quit Program. For when you're tired of aimlessly sorting numbers. Press "y" when prompted!


SORTED OPTIONS: 

"6": Linear Search. Searches the list in a linear manner. Sort the list (action 7) before doing this action; input the number you want to search for in the list to use.
"7": Sort List. Moves the list myList() to a different list uniqueList(), where all the integers are sorted in numerical order. This step is necessary for all of the search functions to work. Input "y" if you want to see the sorted list, and "n" if you do not. 
"9": Recursive Binary Search. A different search method that is faster than Linear Search. Follow the same instructions as Linear Search. 
"10": Iterative Binary Search. A different search method that is faster than Linear Search. Follow the same instructions as Linear Search.

Note: the use of two lists in this program is so that one can remain unsorted at all times, allowing the user to use both unsorted functions and sorted functions simultaneously. The sorted list is necessary because all of the search functions operate in some form of linear manner, 
and they need to have set end, mid, and start points.

WARNING: Failure to follow these instructions will result in an uncontrollable memory leak in your computer that will eventually set it on fire! Just kidding. The program will probably just yell at you and then crash. 



Section 2: Binary Search; How it Works and Why it Matters

	Recursive Binary Search and Iterative Binary Search are the most complex functions in this program. Understanding this may not help you in operating the program, but hey, at least you'll learn something cool!
Binary search methods search the list in two parts at once, with an low point, a midpoint, and high point. 
When the endpoints (the high point and the low point) are equal to the midpoint, the desired number has been found. This method of searching is twice as fast as Linear Search, as it is conquering two sections of the list at once. 
	Binary search methods do need a few things to function properly. One, it needs a sorted data set, which is a data set that is organized in alphabetical or numeric order. Secondly, it needs defined high, low, and mid points 
to properly search; this can be achieved with a relatively simple algorithm. Some limitations of Binary Search methods include that they cannot search unsorted data, they can only return one instance of the data point that is being searched for, 
and that it only outputs the first instance of the data point in the data set.
	Recursive Binary Search works by creating a function that acts to respond to itself. This action is sorting through the data points, and moving the endpoints and midpoint accordingly. 
The recursion must stop when the desired data point is reached, as there will be no other data points left.
	Iterative Binary Search works by iterating through the data points until it finds the desired data point. This differs from Recursive Binary Search due to the fact that it is running through the list in a linear fashion 
between the midpoint and the endpoints instead of at random. When the desired number is reached, iteration will automatically stop. 

	
Section 3: What I've Changed 

	While this code is quite comprehensive, I noticed that there is no way to remove numbers, only add them! This is an issue if you, the user, accidentally add some integers that you do not want. The code for 
this is shown here: 

def removeNumber():
        print("We're gonna remove some numbers here!") 

        removeItem = input("What number do you want to remove?     ")
        removeItem = int(removeItem)
        
        while removeItem in myList:
            position = myList.index(int(removeItem))
            myList.pop(position)
        print ("The requested numbers have been removed!  ")

	This code is used to remove individual user-specified integers from the list. The code to clear the list entirely is as follows:
 
def clearList(): 
    clear = input ("Are you sure you want to clear the list? Y/N    ")
    if clear.lower() == "y":
        list.clear(myList)
        print ("The list has been cleared!")
    else:
        print ("Action Canceled")

That's about it. Following these instructions exactly will result in complete user satisfaction, and if you're not satisfied, well, at least you can't sue us. 

We here at Kilometer Studios sincerely hope that you enjoy our code and it's many features to their fullest extent! 
  
