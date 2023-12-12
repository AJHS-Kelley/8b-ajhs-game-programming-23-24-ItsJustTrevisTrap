# Hangman Game by Trevis Brown, v0.1
import random
# words = ['Acid Knife Bones Bleach Reptile Banshee Spirit Spider Snake Disease Skull Photosynthesis Mental Flatline Havoc Yamaha Glove Lime Green Teal Eyes Teeth Cell Blood Phobia Venus Saturn Kawasaki Kill Wendigo'].split()
# DICTIONARY VERSION
# Stored in Key: Value Pairs.
# Actual Dictionary Word (Key) : Value (Definition)
# Uses {} to specify a dictionary.
words = {'Colors': 'green lime yellow blue cyan indigo black gold white silver navy grey orange teal'.split(),
         'Animals': 'gecko shark parrot ant cat jellyfish spider mantis iguana bee wasp zebra hyena panda'.split(),
         'Shapes': 'square triangle circle cube trapizoid sphere diamond rectangle octogon'.split(),
         'Foods': 'fries milkshake apple pineapple grape watermelon lemon lime kiwi corn dragonfruit strawberry'.split()}


#VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |    
        |
        |    
    =========''','''
    +---+
    O   |    
        |
        |    
    =========''','''
    +---+
    O   |    
    |   |
        |    
    =========''','''
    +---+
    O   |    
   /|   |
        |    
    =========''','''
    +---+
    O   |    
   /|\  |
        |    
    =========''','''
    +---+
    O   |    
   /|\  |
   /    |    
    =========''','''
    +---+
    O   |    
   /|\  |
   / \  |    
    =========''','''
    +---+
    O   |    
  o-|-o |
   / \  |    
    =========''','''
    +---+
    O   |    
  o-|-o |
   / \  |
  o   o |
    =========''']
  
# Pick Word from List
# def getRandomWord(wordlist): # Return a random word from the list.
#     wordIndex = random.randint(0, len(wordList) - 1)
#     # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
#     return wordList[wordIndex]

def getRandomWord(wordDict): # Return a random word from the list.
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey] - 1))
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()

    blanks = '_' * len(secretWord)
    
    # Replace Blanks with Correct letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()             


def getGuess(alreadyGuesed):
    while True:
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuesed:
            print('Letter has been guessed already, try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the English alphabet')
        else:
            return guess
        
def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith('y')

# Introduce the Game
print('Welcome to the Game by Trevis.')

# Choose Difficulty
difficulty = 'X'
while difficulty not in 'EMH':
    print('Please Choose Easy, Medium, or Hard. Type the first letter then press enter.\n')
    difficulty = input().upper()
if difficulty == 'M': # Medium
    del HANGMAN_BOARD[]
    del HANGMAN_BOARD[]
if difficulty == 'H'
    del HANGMAN_BOARD[]
    del HANGMAN_BOARD[]
    del HANGMAN_BOARD[]
    del HANGMAN_BOARD[]


missedLetters = ' '
correctLetters = ' '
secretWord = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check To See If Winner, Winner Chicken Dinner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:  # if True:
                print('Imagine Winning, Could not be Me.')
                print('The secret word was' + secretWord)
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == lens(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game.')
            print('You made this number of correct guesses' + str(len(correctLetters)))
            print('the secret word was' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ' '
            correctLetters = ' '
            
# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1




