import random 

computer = random.choice(["Snake","Water""Gun"])
user = input("Enter your choice: ")

if user == computer:
    print("It's a tie!")
else:
    if (user == "Snake") and (computer == "Water"):
        print("Snake drinks water and dies. You win!")

    elif(user == "Snake") and (computer == "Gun"):
        print("Gun shoots snake and snake dies. You lose!")

    elif(user == "Water") and (computer == "Gun"):
        print("Gun cannot shoot water. You win!")

    elif(user == ""):
        pass
    