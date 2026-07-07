import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = {}
computer = {}

def score(dic):
    x=0
    for i in dic :
        x += dic[i]
    return x
def pick(dic):
    x = len(dic)
    dic[f"card{x+1}"]=random.choice(cards)
def result():
    if score(player) > score(computer) and score(player) < 21:
        print(f"Your score is {score(player)}, computer score is {score(computer)} \n YOU WIN!!")
    elif score(player) > 21:
        print(f"Your score is {score(player)} \nYou went over 21 \nYou lose :(")
    elif score(player) == score(computer):
        print(f"Your score: {score_player} \nDraw......")
    elif score(computer) > 21 and score(player) < 21:
        print(f"YOU WIN!! \nyour score {score(player)} \ncomputer score {score(computer)} it went over 21 ")
    elif score(player) == 21:
        print(f"BLACKJACK!!! YOU WIN!!!! \ncomputer score {score(computer)} ")
    elif score(computer) > score(player) and score(computer) <= 21:
        print(f"you lose :( \ncomputer score {score(computer)} your score {score(player)} ")

    else:
        print(score(player), score(computer))
        print("Exception")

choice = ["pick", "hold"]
def computer_choice():
    if score_computer < 21:
        choice_computer = random.choice(choice)
        if choice_computer == "pick":
            pick(computer)

while True:
    i = 0
    while i < 2:
        i += 1
        player[f"card{i}"] = random.choice(cards)
        computer[f"card{i}"] = random.choice(cards)
    score_player = score(player)
    score_computer = score(computer)
    print(f"your current hand card_1: {player['card1']}, card_2: {player['card2']} \nfirst card of computer is: {computer['card1']} \ncurrent_score = {score(player)}")
    choice_str = input("Would you pick a card or hold? (pick/hold): \n").lower().lstrip()
    if choice_str == "hold":
        computer_choice()
        result()
    else:
        pick(player)
        x = len(player)
        print(f"Your pick is: {player[f'card{x}']}")
        computer_choice()
        result()
    choice = input("continue? (y/n): ").lower().lstrip()
    if choice == "y":
        print("continuing....... \n")
        player= {}
        computer = {}
    else:
        print("Goodbye........ \n:3")
        break
