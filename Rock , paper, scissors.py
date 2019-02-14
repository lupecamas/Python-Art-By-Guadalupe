import random

choice_list = ['Paper','Rock','Scissors']
random_ch = random.SystemRandom()
choice = random.choice(choice_list)


print("Let's play Rock,Paper,Sissors?")
playagain = input("Do you want to play?").lower()
while (playagain == "yes" or playagain == "y"):

      
#user_input1
    answer =input ().lower()
#paper
    print (choice)
    if answer == "paper" and choice == "Paper":

        print ("It's a tie")
        playagain = input("Do you want to play?").lower()
    elif answer == "paper" and choice == "Scissors":
 
        print ("I win ")
        playagain = input("Do you want to play?").lower()
    elif answer == "paper" and choice == "Rock":
        print(' YOU WIN')
        playagain = input("Do you want to play?").lower()



#---------------------------------------------------------------------------------------------

#ROCK

    if answer == "rock" and choice == "Rock":
        print ("It's a tie")
        playagain = input("Do you want to play?").lower()

    elif answer == "rock" and choice == "Scissors":
        print ("You win")
        playagain = input("Do you want to play?").lower()


    elif answer == "rock" and choice == "Paper":
        print (" I win")
        playagain = input("Do you want to play?").lower()

#-----------------------------------------------------------------------------
#Scissors
    if answer == "scissors" and choice == "Scissors":
        print ("It's a tie")
        playagain = input("Do you want to play?").lower()
    elif answer == "scissors" and choice == "Paper":
        print ("You win")
        playagain = input("Do you want to play?").lower()
    elif answer == "scissors" and choice == "Rock":
        print ("I win")

print("Goodbye.")








    
