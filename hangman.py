import random
import string
from words import words
def hangman_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()    
def hangman():
    word = hangman_word(words)
    print(word)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 5
    while len(word_letters) > 0 and lives > 0 :
        print(f"{lives}Lives has left. ""You used these letters", "".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word = ", "".join(word_list))
        user_letter = input("Guess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word.You have lost one of your lives :)")

        elif user_letter in used_letters:
            print("You have already used that character.Please try again.")
        else:
            print("Invalid character.Please try again.")
    if lives == 0:
        print("You are dead !!. The word was " + str(word))
    else :
        print("You guseed the word Correct Nice one ! "+str(word))
hangman()