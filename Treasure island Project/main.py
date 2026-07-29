print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('you\'re ar a cross word, where do you want to go?' 'Type "left" or "right:"').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to lake' 'There is island in the Middle of the lake' 'Type "wait" to wait for a bot' 'Type "swim" to swim areas:').lower()

    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed" "There is house with 3 doors. one red," "one yellow and one blue." "which colour do you choose?:").lower()

        if choice3 == "red":
            print("Its a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found a treasure. You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over")
        else:
            print("You choose a door that doesn't exist. Game over")
    else:
        print("You got attacked by an angry trout. Game over.")

else:
    print("You fell in to a hole. Game over")

