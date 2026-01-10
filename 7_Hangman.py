# using for & while loops, lists, String, Range, Modules.
import random

words_list = [
    "apple", "banana", "ball", "beach", "bear", "bird", "birdhouse", "blanket",
    "blue", "box", "cake", "camel", "car", "carrot", "castle", "chair", "clock",
    "cloud", "coffee", "coral", "cup", "cupcake", "cupboard", "date", "desk", "dog",
    "dolphin", "elephant", "egg", "flag", "flower", "fox", "giraffe", "gold", "goat",
    "green", "grape", "heart", "hibiscus", "homework", "ice", "icecream", "indigo",
    "jacket", "jasmine", "kangaroo", "lamp", "leaf", "letter", "light", "lion", "magic",
    "milk", "monkey", "moon", "orange", "paper", "peach", "pencil", "picture", "planet",
    "plate", "poppy", "rabbit", "rain", "red", "rose", "sheep", "shoes", "shoe", "spider",
    "star", "starfish", "table", "tiger", "towel", "treasure", "truck", "turtle", "violet",
    "wave", "whale", "window", "wolf", "yellow", "zebra"
    ]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def string_convertor(x):
    result = ""
    for i in x:
        result += i
    return result

print("*********** Welcome to the Hangman Game ***********  ")
word = random.choice(words_list)
# print(word)
guess_word = []
for i in range(0, len(word)):
    guess_word += "_"
print("You have to guess the word ",string_convertor(guess_word))

lives=7
while lives!=0:
    print(f"*******************************{lives}/7 LIVES LEFT ************************************")
    guess_letter = input("Guess a letter : ").lower()
    for i in range(len(word)):
        if word[i] == guess_letter:
            guess_word[i] = guess_letter
    if guess_letter not in word:
        lives-=1
    if lives >= 0 and lives <= 6:
        print(stages[lives])
    print("Guessed word is ", string_convertor(guess_word))
    if string_convertor(guess_word)==word:
        print("Congratulations, You won! It is ",word)
        break

if lives==0:
    print("You lose! 0 lives left.\nThe word is ",word)