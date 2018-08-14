"""
8/14/2018
This program plays rock, paper, scissors against the user. Comes from
a Codecademy exercise.
"""
# getting randint to ultimately decide the computer's choice
from random import randint

# list with possible choices
options = ["ROCK", "PAPER", "SCISSORS"]

# dictionary with messages depending on game results
message = {"tie": "Yawn it's a tie!",
          "won": "Yay you won!",
          "lost": "Aww you lost!"}

# decides the outcome of the game and returns the key
# for the appropriate message
def decide_winner(user_choice, computer_choice):
  print("Your choice is %s" % user_choice)
  print("The computer chose %s" % computer_choice)
  if user_choice == computer_choice:
    return "tie"
  elif user_choice == "ROCK" and computer_choice == "SCISSORS":
    return "won"
  elif user_choice == "SCISSOR" and computer_choice == "PAPER":
    return "won"
  elif user_choice == "PAPER" and computer_choice == "ROCK":
    return "won"
  else:
    return "lost"

# Gets the choices from the computer and the user, then calls
# decide_winner and prints out the appropriate message
def play_RPS():
  user_choice = input("Enter Rock, Paper, or Scissors: ").upper()
  computer_choice = options[randint(0, 2)]
  print(message[decide_winner(user_choice, computer_choice)])

# starting the actual game
play_RPS()
