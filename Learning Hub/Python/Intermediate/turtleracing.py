import turtle
import random

# consants dimensions of screen
WIDTH, HEIGHT = 500, 500
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan", "magenta"]

# get the number of turtles
def get_number_of_turtles():
    while True:
        try:
            num_turtles = int(input("Enter the number of turtles (2-10): "))
            if 2 <= num_turtles <= 10:
                return num_turtles
            else:
                print("Please enter a number between 2 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.") 

# create a turtle screen
def init_turtle():
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.title("Turtle Racing!")
  return screen

def main():
  num_turtles = get_number_of_turtles()
  screen = init_turtle()

  # Create turtles and place them at the starting line
  start_x = -WIDTH//2 + 20
  start_y = HEIGHT//2 - 40
  gap = HEIGHT // (num_turtles + 1)
  racers = []
  for i in range(num_turtles):
      racer = turtle.Turtle()
      racer.shape("turtle")
      racer.color(colors[i])
      racer.penup()
      racer.goto(start_x, start_y - i * gap)
      racer.pendown()
      racer.speed(random.randint(1, 10))
      racers.append(racer)
  
  # Race loop
  finish_line = WIDTH // 2 - 20
  winner = None

  while not winner:
      for racer in racers:
          step = random.randint(1, 10)
          racer.forward(step)
          if racer.xcor() >= finish_line:
              winner = racer
              break

  print(f"The winner is {winner.color()[0]}!")
  screen.mainloop()



main()