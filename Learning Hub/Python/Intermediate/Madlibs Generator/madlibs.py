from pathlib import Path

file_path = Path("Python/Intermediate/Madlibs Generator/story.txt")

with file_path.open(encoding="utf-8") as f:
    story = f.read()

words = set()
start_of_word = -1
target_start = '<'
target_end = '>'

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    elif char == target_end and start_of_word != -1:
        word = story[start_of_word + 1: i] 
        words.add(word)
        start_of_word = -1

answers = {}
for word in words:
    user_input = input(f"Please enter a {word}: ")
    answers[word] = user_input

for key,value in answers.items():
    placeholder = f"<{key}>"
    story = story.replace(placeholder, value)

print(story)