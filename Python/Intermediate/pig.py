import random

def pig_roll():
    return random.randint(1, 6)

# Get number of players
while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit() and 1 <= int(players) <= 4:
        players = int(players)
        break
    else:
        print("Invalid input.")

max_score = 50
player_score = [0 for _ in range(players)]

game_over = False
# play
while not game_over:
    for i in range(players):
        turn_score = 0
        print(f"\nPlayer {i + 1}'s turn:")

        while True:
            roll = pig_roll()
            print(f"You rolled a {roll}.")

            if roll == 1:
                turn_score = 0
                print("Turn over. No points earned this turn.")
                break
            else:
                turn_score += roll
                print(f"Current turn score: {turn_score}")

                while True:
                    choice = input("Roll again or hold? (r/h): ").lower()
                    if choice in ('r', 'h'):
                        break
                    print("Invalid choice. Enter 'r' or 'h'.")

                if choice == 'h':
                    player_score[i] += turn_score
                    print(f"Total score for Player {i + 1}: {player_score[i]}")
                    break

        if player_score[i] >= max_score:
            print(f"\n🎉 Player {i + 1} wins with a score of {player_score[i]}! 🎉")
            game_over = True
            break