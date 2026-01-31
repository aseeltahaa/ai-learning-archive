import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
  user_input = input("Type 'rock', 'paper', 'scissors' or 'quit' to end the game: ").lower()

  if user_input == "quit":
    break

  if user_input not in options:
    print("Invalid input! Please try again.")
    continue

  random_num = random.randint(0, 2)
  computer_input = options[random_num]
  print(f"Computer chose: {computer_input}")

  if(user_input == computer_input):
    print("It's a tie!")
  elif user_input == "rock":
      if computer_input == "scissors":
        print("You win!")
        user_wins += 1
      else:
        print("Computer wins!")
        computer_wins += 1
  elif user_input == "paper":
      if computer_input == "rock":
        print("You win!")
        user_wins += 1
      else:
        print("Computer wins!")
        computer_wins += 1
  elif user_input == "scissors":
      if computer_input == "paper":
        print("You win!")
        user_wins += 1
      else:
        print("Computer wins!")
        computer_wins += 1

print(f"Final score - You: {user_wins}, Computer: {computer_wins}")