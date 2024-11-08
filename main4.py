import random

computer = random.choice([1,2,3])
user_opt = input("Enter your choice: ")
youdict = {"rock":1, "paper":2, "scissors" :3}
reverse_dict = {1: "rock", 2: "paper", 3: "scissors"}
user = youdict[user_opt]

print(f"You chose {reverse_dict[user]}\nComputer chose{reverse_dict[computer]}")

if computer == user:
     print("It's a tie!")

else:
     if(computer == 1) and (user == 2):
          print("Paper covers rock, you win!")

     elif(computer == 2) and (user == 3):
          print("Scissors cuts paper, you win!")
     
     elif(computer == 3) and (user == 1):
          print("Rock crushes scissors, you win!")
     
     elif(computer == 1) and (user == 3):
          print("Rock crushes scissors.You lose!")

     elif(computer == 2) and (user == 1):
          print("Paper covers rock. You lose!")

     elif(computer == 3) and (user == 2):
          print("Scissors cuts paper. You lose!")
          
    


