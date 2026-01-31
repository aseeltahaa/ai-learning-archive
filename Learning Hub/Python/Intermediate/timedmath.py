import random
import time

OPERATORS = ["+", "-", "*", "/"]
MIN_NUMBER = 1
MAX_NUMBER = 10
TOTAL_PROBLEMS = 10

def generate_problem():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)
    
    if operator == "/":
        num1 = num1 * num2
    
    problem = f"{num1} {operator} {num2}"
    answer = eval(problem)
    return problem, answer

wrong = 0
input("Press Enter to start the Timed Math Challenge...")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    problem, answer = generate_problem()
    print(f"Problem #{i + 1}: {problem} = ?")

    while True:
      user_answer = float(input("Your answer: "))
      if user_answer == answer:
          break

end_time = time.time()
total_time = end_time - start_time
print("------------------------------")
print("Nice work!")
print(f"You finished in {total_time:.2f} seconds!")