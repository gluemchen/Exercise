import random

function = ["rock", "paper", "scissor"]
wins_player = 0
wins_cpu = 0
turns = 0
play_again = ""


while True:
    turns == 0
    if wins_player > wins_cpu:
        print("You won! Score: ", wins_player, ":", wins_cpu)
        break
    elif wins_cpu > wins_player:
        print("You lost! Score: ", wins_cpu, ":", wins_player)
        break
    elif wins_cpu == wins_player:
        print("We have a draw! Score: ", wins_cpu, ":", wins_player)
        play_again = str(input("Do you wish to play again?(y/n): "))
        if play_again == "y":
            print("Let's give it another go!")
            continue
        elif play_again == "n":
            print("It was fun. Have a nice day!")
            break
        elif play_again != "y" or "n":
            print("Seems you didn't hit the right keys!")
        break
    else:
        print("ERROR")
