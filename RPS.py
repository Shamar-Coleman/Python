import random

print("Welcome to ROCK! PAPER! SCISSORS! Pick wisely...")

playerPoints = 0
cpuPoints = 0

while playerPoints != 3 and cpuPoints != 3:

    your_choice = input("Enter a choice(rock, paper, scissors): ")
    user_selection = ["rock", "paper", "scissors"]
    cpu_selection = random.choice(user_selection)

    print(
        f"\nUser selection: {your_choice}, Opponent chose {cpu_selection}.\n")

    if your_choice == cpu_selection:
        print("draw!!!.. try again, this time with WIN!")
    elif your_choice == "rock":
        if cpu_selection == "scissors":
            print("Smell what the Rock is cooking! You win!")
            playerPoints += 1
        else:
            print(
                "Paper beats rock, wrapped up. \nBetter luck next time!")
            cpuPoints += 1
    elif your_choice == "paper":
        if cpu_selection == "rock":
            print("Paper beats rock... PAPER! You win!!!")
            playerPoints += 1
        else:
            print("Scissors beats paper duh! \nNice.")
            cpuPoints += 1
    elif your_choice == "scissors":
        if cpu_selection == "paper":
            print("Scissors beats paper, Easy slice!")
            playerPoints += 1
        else:
            print(
                "You fool! Rocks victory! \nBetter luck next time...")
            cpuPoints += 1

if playerPoints > cpuPoints:
    print(f"{playerPoints} VS {cpuPoints} You win!")
else:
    print(f"{playerPoints} VS {cpuPoints} Better luck next time!")