import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("enter a number between 0 to 2\n"))
computer_choice = random.randint(0,2)
print(f"user chooses: {game_images[user_choice]}")
print(f"computer chooses: {game_images[computer_choice]}")
if user_choice>=3 or user_choice<0:
    print("Invalid number try again")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice==2 and computer_choice==0:
    print("You lose!")
elif user_choice>computer_choice:
    print("you win")
elif user_choice<computer_choice:
    print("you lose!")
elif user_choice == computer_choice:
    print("its a draw")