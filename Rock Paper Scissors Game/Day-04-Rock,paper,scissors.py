rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choices = ["Rock", "paper", "Scissors"]

user = input("Enter rock,paper, or scissors: ").lower()
computer = random.choice(choices)

print("computer: ",computer)

if user == computer:
    print("Draw")

elif user == "rock":
    if computer == "Scissors":
        print("You win")
    else:
        print("You lose")

elif user == "Paper":
    if computer == "rock":
        print("You win")
    else:
        print("You Lose")

elif user == "scissors":
    if computer == "paper":
        print("You win")
    else:
        print("You lose")

else:
    print("Invalid Input") 
