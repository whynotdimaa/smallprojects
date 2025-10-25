import random


def rock_paper_scissors():
    wins = 0
    draws = 0
    losses = 0
    while True:
        choice = int(input('1.rockpaperscissors\n2.exit\n'))
        if choice == 1:
            computer_choice = random.choice(["rock", "paper", "scissor"])
            human_choice = input("Rock, Paper, Scissor?\n")
            print(computer_choice)
            if computer_choice == human_choice:
                print("draw")
                draws += 1
                continue
            if human_choice == "rock":
                if computer_choice == "paper":
                    print("You lose")
                    losses += 1
                else:
                    print("You Win")
                    wins += 1
            elif human_choice == "paper":
                if computer_choice == "scissor":
                    print("You lose")
                    losses += 1
                else:
                    print("You win")
                    wins += 1
            elif human_choice == "scissor":
                if computer_choice == "rock":
                    print("You lose")
                    losses += 1
                else:
                    print("You win")
                    wins += 1
        elif choice == 2:
            print(f"Перемоги : {wins}")
            print(f"Програші : {losses}")
            print(f"Нічия : {draws}")
            break


rock_paper_scissors()
