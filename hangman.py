# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    for i in letters_guessed:
        if i in secret_word:
            count += 1
    if count == len(secret_word):
        return True
    else:
        return False
            


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = []
    for i in secret_word:
        if i in letters_guessed:
            word.append(i)
        else:
            word.append("*")

    return "".join(word)

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = []
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabets:
        if i not in letters_guessed:
            letters.append(i)
    return "".join(letters)



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Hello, lets start...")
    print(f"the word contains number of letters {len(secret_word)}")
    print("you can start with 10 guesses")
    no_of_guesses = 10
    guessed_letters = []
    alphabets = string.ascii_lowercase
    vowels = "aeiou"
    consonents = "".join([c for c in alphabets if c not in vowels ])

    while(no_of_guesses > 0):
        print(f"the number of guesses left {no_of_guesses}")
        available_letters = get_available_letters(guessed_letters)
        print(f"the available letters are {available_letters}")
        guessed_character = input("Guess the letter: ")
        if(guessed_character == "#"):
            return
        if(guessed_character == "!"):
            with_help = True

        if(with_help == False):
          if(len(guessed_character) > 1):
              print("Only one character per guess pls..")
              return
          if(guessed_character in guessed_letters):
              print("the letter is already guessed.")
          elif(guessed_character in secret_word):
              guessed_letters.append(guessed_character)
              print("Good!, right guess..")
              no_of_guesses -= 1
          else:
              if guessed_character in consonents:
                no_of_guesses -= 1
              else:
                  no_of_guesses -= 3
              print("Oops!, wrong guess...")
        else:
            if(no_of_guesses < 3):
                print(f"Sorry, you don't have enough guesses left for a hint, the word is{secret_word}")
            else:
              guessed_word = get_word_progress(secret_word, guessed_letters)
              indexes = []
              for index, char in enumerate(guessed_word):
                  if(char == "*"):
                      indexes.append(index)
              random_number = random.choice(indexes)
              revealing_word = secret_word[random_number]
              guessed_letters.append(revealing_word)
              get_word_progress(secret_word, guessed_letters)
              no_of_guesses -= 3


        print("Game progress...")
        print(get_word_progress(secret_word, guessed_letters))
        if(has_player_won(secret_word, guessed_letters)):
            print(f"Congragulations you won!, the word is {secret_word}")
        elif(no_of_guesses == 0 and not has_player_won(secret_word, guessed_letters)):
            print(f"Sorry! you lost..., the correct word is {secret_word}")
            

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.


