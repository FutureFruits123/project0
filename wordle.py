"""
Randomizes a word from a list of possible words and plays a game of Wordle with the user, allowing them to guess the word in 6 tries.

The `randomizeWord()` function selects a random word from the `possibleWords` list and stores it in the `word` variable.

The `playGame()` function runs the main Wordle game loop. It prompts the user to guess a word, checks the guess against the randomly selected word, and provides feedback on the correctness of the guess. The game continues until the user correctly guesses the word or runs out of attempts.
"""
import random

def randomizeWord():
  global possibleWords
  global word
  possibleWords = ["water", "apple", "chair", "flame", "blaze", "clock", "piece", "fruit", "sword", "rifle", "house", "crain", "world", "range", "night", "heavy", "earth", "light", "obese", "music", "space", "heart", "class", "brass", "power", "green", "river", "field", "plant", "floor", "plane", "grain", "child", "human", "party", "blood", "shape", "ocean", "grass", "glass", "women", "level", "stone"]
  word = possibleWords[random.randrange(0, len(possibleWords))]

def playGame(wordleComplete):
  while wordleComplete == False:
    randomizeWord()
    print("Let's play Wordle! Guess the word in 6 tries. Each guess must be a valid 5-letter word. For each guess, a hint will tell you how many letters you've guessed correctly. A G represents a letter in the word and in the correct spot.. A Y represents a letter in the word but in the wrong spot. A - represents a letter not in the word in any spot. Guess below!")
    def makeAGuess(userGuess):
      hint = ""

      for i in range(len(word)):
        if word[i] == userGuess[i]:
          hint += "G"
        elif userGuess[i] in word:
          hint += "Y"
        else:
          hint += "-"

      return hint

    for i in range(6):
      guess = input("What word would you like to guess? Make sure your guess is lowercase.")
      hint = makeAGuess(guess)
    
      print(hint)
    
      if hint == "GGGGG":
        print("You guessed the word!")
        return

    if hint != "GGGGG":
      print("You failed to guess the word. The word was " + word + ".\n")