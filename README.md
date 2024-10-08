# Hangman-Game_Code-Alpha
*Hangman Game*
This is a simple command-line Hangman game written in Python. In this game, the player tries to guess a randomly selected word, letter by letter. Each incorrect guess results in a part of the hangman being drawn. The game ends either when the player correctly guesses the word or the hangman is fully drawn after 7 incorrect guesses.

*Key Features:*

1. Random Word Generation: The game uses the Faker library to generate random words for each new game.
2. Dynamic Word Display: After each correct guess, the word is updated in real-time, showing the correctly guessed letters.
3. Visual Representation: The hangman is visually drawn step by step for every incorrect guess.
4. Unlimited Play: The player can start a new game after finishing one by simply restarting the program.
   
*How to Play:*

1. Run the script, and a word with hidden letters will be displayed.
2. Input one letter per turn to guess the word.
3.  For each correct guess, the word will update with the guessed letters in their correct positions.
4. For each incorrect guess, a part of the hangman will be drawn.
5. You win the game by guessing all the letters correctly before the hangman is fully drawn.
6. You lose if the entire hangman is drawn before the word is guessed.
   
*Requirements:*

1. Python 3.x
2. faker library (pip install faker)
