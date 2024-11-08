import random 

computer = random.choice([1,2,3])
pc_dict = {1 : "rock", 2:"paper", 3: "scissors"}
user = int(input("1. Rock\n2. Paper\n3. Scissors\nEnter your choice(1,2,3): "))
#user_dict = {}
print(f"You chose : {pc_dict[user]}")
print("The computer chose :", pc_dict[computer])
if user == computer:
    print("It's a tie!")
else:
    if (user == 1) and (computer == 2):
        print("Rock tear apart the paper. You win!")

    elif(user == 1) and (computer == 3):
        print("Rock destroys the scissors. You win!")

    elif(user == 2) and (computer == 1):
        print("Paper gets destroyed by the rock. You lose!")

    elif(user == 2) and (computer == 3):
        print("Scissors cuts down the paper. You lose!")
    
    elif(user == 3) and (computer == 1):
        print("Rock crushes the scissors. You lose!")
    
    elif(user == 3) and (computer == 2):
        print("Scissors cuts the paper. You win!")

    else:
        print("Something went wrong")