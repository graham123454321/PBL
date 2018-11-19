import random #allows for me to use the random function which is useful in these tasks
dice = 6 #shows the number of sides on the dice
dice_list = [] #blank list where the rolls can be added to.
rolls = int(input("How many times would you like to roll the dice")) #lets user decide how many times to roll dice
def sumdice(dice,rolls):
    for x in range(rolls): #tMakes sure the dice will only be rolled the amount of times the user imputed
        dicerolls = random.randint(1, dice) #selects a random number between 1 and 6 that can be rolled
        dice_list.append(dicerolls) #adds the number that was rolled to the blank list
    print("you have ", + dice_list.count(1), " ones") #counts how many of each number you have and then prints it
    print("you have ", + dice_list.count(2), " twos")
    print("you have ", + dice_list.count(3), " threes")
    print("you have ", + dice_list.count(4), " fours")
    print("you have ", + dice_list.count(5), " fives")
    print("you have ", + dice_list.count(6), " sixes")
sumdice(dice,rolls) #calls the function


print("         ")
print("next task") #provides spacing between the tasks
print("         ")

shoplist = [] #blank list which allows for items to be added to it
y = 1
while y == 1: #allows the function to run when it is at this set value
    shop = input("Would you like to add something to your shopping list?") #lets user chose to add items to the list
    if shop == "no":
        print("Alright thanks for stopping by the store.")
        print(shoplist) #prints all the items that were imputed at once
        y = y + 2 #stops the function from running as the value is changed
    elif shop == "yes":
        shopping = input("What would you like to add to the list")
        shoplist.append(shopping) #adds an item to the physical list

print("         ")
print("next task") #provides spacing between the tasks
print("         ")


inlist = [2, 3, 7, 4, 5, 99, 100] #the list of possible numbers
print(inlist) #prints this list to show user all possible numbers
def large_value(inlist):
    inlist.sort() #sorts the values of the list from least to greatest
    return inlist[len(inlist) - 1] #will return every number in the list except for the last one which will be the largest one
print("The biggest number in the list is " + str(large_value(inlist)))
'''the last line calls the function and tells the user what the biggest number is'''

print("         ")
print("next task") #provides spacing between the tasks
print("         ")


list_1 = [2, 5, 7, 9] #an intial list
list_2 = [1, 3, 4, 6, 8] #an initial list

def mergelist(list_1, list_2):
    lists = list_1 + list_2 #will merge the two lists together
    newlist = [] #A new list where the numbers can be placed once sorted
    for x in range(0, len(lists)): #lets the program run for every number in the list
        newlist.insert(0,max(lists)) #selects the larget number from the two lists and puts it in the new list
        lists.remove(max(lists)) #removes the largest number from the merged list, which will be the number just added to the list
    return newlist #stores the value of the new list

print("the first list is " + str(list_1)) #allows for you to see what the first list was
print("the second list is " + str(list_2)) #allows for you to see what the second list was
print("the two list merged together are " + str(mergelist(list_1, list_2))) #shows the two lists merged together in numerical order


print("         ")
print("next task")#provides spacing between the tasks
print("         ")

inlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #all possible numbers
inlist2 = [] #allows for numbers to be placed in a new list, so they can be printed at the end
def piviotlist(inlist, number):
    for x in range(len(inlist)): #sets the program to run as many times as there are values in the list
        if number > inlist[x]: #will add any values that are less then the inputed number to the new list
            inlist2.append(inlist[x]) #will add the value to the open list
    return inlist2 #saves the values to the open list
print(piviotlist(inlist, int(input("Gimme a number")))) #allows user to detmine the cut off of what numbers will be shown


player_list = [[],[],[],[]] #a blank list that will hold the values of the dice

roll_amount = int(input("How many times would you have like to roll the dice ")) #allows for the user to determine how may times to roll the dice
for y in range(4): #rolls everything 4 times as there are 4 players
    for x in range(roll_amount): #rolls the dice the number of times selected by the user
        player_list[y].append(random.randint(1, 6)) #randomly determines the numbers of the rolls
print(player_list) #prints the list of numbers rolled for all players

print("         ")
print("next task") #provides spacing between the tasks
print("         ")

''' this allows for it to check if you win. If either x or o have three in a row it will retun win. otherwise it will return
0 and allow for it to keep checking the function'''
def win_check (tic_tac_toe_list1):
    if tic_tac_toe_list1[0][0] == tic_tac_toe_list1[0][1] == tic_tac_toe_list1[0][2]:
        return ("win")
    elif tic_tac_toe_list1[1][0] == tic_tac_toe_list1[1][1] == tic_tac_toe_list1[1][2]:
        return ("win")
    elif tic_tac_toe_list1[2][0] == tic_tac_toe_list1[2][1] == tic_tac_toe_list1[2][2]:
        return("win")
    elif tic_tac_toe_list1[0][0] == tic_tac_toe_list1[1][0] == tic_tac_toe_list1[2][0]:
        return("win")
    elif tic_tac_toe_list1[0][1] == tic_tac_toe_list1[1][1] == tic_tac_toe_list1[2][1]:
        return("win")
    elif tic_tac_toe_list1[0][2] == tic_tac_toe_list1[1][2] == tic_tac_toe_list1[2][2]:
        return ("win")
    elif tic_tac_toe_list1[0][0] == tic_tac_toe_list1[1][1] == tic_tac_toe_list1[2][2]:
        return ("win")
    elif tic_tac_toe_list1[0][2] == tic_tac_toe_list1[1][1] == tic_tac_toe_list1[2][0]:
        return("win")
    else:
        return 0


tic_tac_toe_list1 = [[1,2,3], [4,5,6], [7,8,9]] #a list of stored values which will determine where you want to move
for x in tic_tac_toe_list1:
    print(x) #prints list showing players possible options
for l in range(5): #allows for it to run 9 times for the 9 possible spaces
    y = 0 #set value which will allow for you to switch players
    c = 1 #set value which will allow for you to switch players
    while y == 0: #player x will run when y is equal to 0
        play = input("Where would you like to move")
        if play == "1": #allows for you to place an x in the certain a certain location and that is the same as below
            tic_tac_toe_list1[0][0] = "x"
        elif play == "2":
            tic_tac_toe_list1[0][1] = "x"
        elif play == "3":
            tic_tac_toe_list1[0][2] = "x"
        elif play == "4":
            tic_tac_toe_list1[1][0] = "x"
        elif play == "5":
            tic_tac_toe_list1[1][1] = "x"
        elif play == "6":
            tic_tac_toe_list1[1][2] = "x"
        elif play == "7":
            tic_tac_toe_list1[2][0] = "x"
        elif play == "8":
            tic_tac_toe_list1[2][1] = "x"
        elif play == "9":
            tic_tac_toe_list1[2][2] = "x"
        for x in tic_tac_toe_list1:
            print(x) #will print the new list with the o instead of the number selected
        y = y + 1 #chnages y value you so it can't be run
        c = c - 1 #changes c value which allows for it to run
    if win_check(tic_tac_toe_list1) == "win":
         break #if you win the game will end
    while c == 0:
        play = input("Where would you like to move")
        if play == "1": #allows for you to place an o in the certain a certain location and that is the same as below
            tic_tac_toe_list1[0][0] = "o"
        elif play == "2":
            tic_tac_toe_list1[0][1] = "o"
        elif play == "3":
            tic_tac_toe_list1[0][2] = "o"
        elif play == "4":
            tic_tac_toe_list1[1][0] = "o"
        elif play == "5":
            tic_tac_toe_list1[1][1] = "o"
        elif play == "6":
            tic_tac_toe_list1[1][2] = "o"
        elif play == "7":
            tic_tac_toe_list1[2][0] = "o"
        elif play == "8":
            tic_tac_toe_list1[2][1] = "o"
        elif play == "9":
            tic_tac_toe_list1[2][2] = "o"
        for x in tic_tac_toe_list1: #will print the new list with the o instead of the number selected
            print(x)
        y = y - 1  # changes y value which allows for it to run
        c = c + 1  # chnages c value you so it can't be run
    if win_check(tic_tac_toe_list1) == "win": #if you win the game will end
         break















