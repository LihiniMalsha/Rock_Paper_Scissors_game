# じゃん拳ぽん ゲーム　（rock, paper, scissors game）

import random

choices = ["rock", "paper", "scissors"]
running = True

while running:

    player = None
    computer = random.choice(choices)

    while player not in choices:
          player = input("Enter a choice (rock,paper,scissors):").lower()

    print("player: " + player)
    print("computer: " + computer)

    if player == computer:
        print("It's s tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("play again?(yes or no): ").lower()
    if not play_again == "yes":
        running = False
        print("Thanks for playing and Good bye!")
