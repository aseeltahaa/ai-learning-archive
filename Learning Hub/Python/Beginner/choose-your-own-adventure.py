name = input("Enter your name: ")
print(f"Welcome, {name}, to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go either left or right. Which way would you like to go? (left/right) ").lower()

if(answer == "left"):
    answer = input("You come to a river, you can walk around it or swim across? (walk/swim) ").lower()
    if(answer == "swim"):
        print("You swam across and were eaten by an alligator. Game Over!")
    elif(answer == "walk"):
        print("You walked for miles, ran out of water and lost the game. Game Over!")
    else:
        print("Not a valid option. Game Over!")

elif(answer == "right"):
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back? (cross/back) ").lower()
    if(answer == "cross"):
        print("You crossed the bridge and found a treasure chest! You win!")
    elif(answer == "back"):
        print("You went back and got lost in the woods. Game Over!")
    else:
        print("Not a valid option. Game Over!")
        
else:
    print("Not a valid option. Game Over!")