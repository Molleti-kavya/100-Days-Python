import random
logo ="""
 _______               ___.                         ________                             
 \      \  __ __  _____\_ |__   ___________        /  _____/ __ __   ____   ______ ______
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \      /   \  ___|  |  \_/ __ \ /  ___//  ___/
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/      \    \_\  \  |  /\  ___/ \___ \ \___ \ 
\____|__  /____/|__|_|  /___  /\___  >__|          \______  /____/  \___  >____  >____  >
        \/            \/    \/     \/                     \/            \/     \/     \/ 
"""

should_play = True
#print(Number)
def number_guess():
    print(logo)
    Number = random.randint(1,100)
    print(" *** Welcome to the Number Guessing Game! *** ")
    print("I'm thinking of a number between 1 and 100")

    level = input("Choose a difficulty type 'easy' or 'hard'.").lower()
    if level == "easy":
         attempt = 10
    else: attempt = 5

    while not attempt <= 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > Number:
            print("Too High")
            print("Guess again")
        elif guess < Number:
            print("Too low")
            print("Guess again")
        elif guess == Number:
            print(f"You got it! The answer was {Number}.\n  *** Congratulations! ***")
            break
        attempt -= 1

while should_play:
    play = input("Do you want to play \"Number Guessing Game\" type 'yes' or 'no' : ").lower()
    if play == 'yes':
        print("\n"*20)
        number_guess()
        should_play = True
    else :
        should_play = False