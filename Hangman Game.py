import random
from faker import Faker
def hangman():
    HANGMAN = [
    r'''
    +---+
    |   |
        |
        |
        |
        |
    =========''', 
    r'''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', 
    r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', 
    r'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', 
    r'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', 
    r'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', 
    r'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']
    guesses = 7
    update = 0
    fake = Faker()
    choseword = fake.word()
    newword = ['_' for _ in choseword]
    print(''.join(newword))
    while guesses > 0:
        a = input("Enter your guess: ")
        if a in choseword:
            print("Correct!")
            for i, letter in enumerate(choseword):
                if letter == a:
                    newword[i] = a
            word = ''.join(newword)
            print(word)
            print("Guesses left: ", guesses)
            if '_' not in word:
                print("Congratulations! You've guessed the word.")
                break
        else:
            print("Incorrect!")
            guesses -= 1
            print(HANGMAN[update])
            update += 1
            print("Guesses left: ", guesses)
            if (guesses==0):
                print("Sorry, you lost!")
    print("\nThe word was", choseword)
hangman()
