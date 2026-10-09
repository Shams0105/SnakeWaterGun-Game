'''
1 = Snake
-1 = Water
0 = Gun
'''
import random  # for computer choice we use random library(not random.randint())

computer = random.choice([1, -1, 0])  # computer choice
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")  # user choice

youDict = {"s": 1, "w": -1, "g": 0}  # dictionary for user choice
you = youDict[youstr]  # user choice in integer

#Now we have 2 choices , now we can check the winner using the game logic

if(computer == you):
    print("Its a Draw")
else:
    if(computer == -1 and you == 1): #Snake vs Water = Snake
        print("You win!!")

    elif(computer == -1 and you == 0): #Water vs Gun = Gun
        print("You Lose!!")

    elif(computer == 1 and  you == 0): #Snake vs Gun
        print("You Win!!")

    elif(computer == 1 and you == -1): #Snake vs Water
        print("You Lose!!")

    elif(computer == 0 and you == 1):  #Gun vs Snake
        print("You Win!!")

    elif(computer == 0 and you == -1): #Gun vs Water
        print("You Lose!!")

    else:
        print("Something went wrong!")