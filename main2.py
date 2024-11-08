import random 

computer = random.choice(["Rock","Paper","Scissors"])
user = input("Enter your choice: ")
print("The computer chose :", computer)
if user == computer:
    print("It's a tie!")
else:
    if (user == "Rock") and (computer == "Paper"):
        print("Rock tear apart the paper. You win!")

    elif(user == "Rock") and (computer == "Scissors"):
        print("Rock destroys the scissors. You win!")

    elif(user == "Paper") and (computer == "Rock"):
        print("Paper gets destroyed by the rock. You lose!")

    elif(user == "Paper") and (computer == "Scissors"):
        print("Scissors cuts down the paper. You lose!")
    
    elif(user == "Scissors") and (computer == "Rock"):
        print("Rock crushes the scissors. You lose!")
    
    elif(user == "Scissors") and (computer == "Paper"):
        print("Scissors cuts the paper. You win!")

    else:
        print("Something went wrong")