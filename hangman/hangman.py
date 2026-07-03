import random
from word_list import word_list
lives = 6
word = random.choice(word_list)

blanks = ""
for letter in word:
    blanks += "_"

print(f"word to guess: {blanks} and is of {len(blanks)} letters") 
while lives != 0 and "_" in blanks:
    guess = input("guess a letter: ").lower()
    if guess in word:
        for index, i in enumerate(word):
            if guess == i:
                blanks = blanks[:index] + guess + blanks[index + 1:]
                print(blanks)
    else:
        lives -= 1
        print(f"you have {lives} lives left")
        print(blanks)
        
if lives == 0:
    print(f"You LOSE!!! The word was {word.upper()}")
else:
    if blanks == word:
        print("YOU HAVE WON!!!")
