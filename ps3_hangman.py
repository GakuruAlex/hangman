import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

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
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all([char in lettersGuessed for char in list(secretWord)])


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    working_secret_word = secretWord
    for letter in working_secret_word:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter, "_")
    return secretWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = "abcdefghijklmnopqrstuvwxyz"
    return "".join([letter for letter in list(available) if letter not in available])

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''




def main() -> None:

    # secretWord = chooseWord(wordlist).lower()
    # print("Secret word is: "+secretWord)
    # lettersGuessed = []
    # br = "-------------"
    # num_of_guesses = 8
    # print("Welcome to the game, Hangman!\nI am thinking of a word that is " + len(secretWord)+  "letters long.")
    # print(br)
    # while num_of_guesses > 0:
    #     available_letters = getAvailableLetters(lettersGuessed=lettersGuessed)
    #     print("You have "+num_of_guesses+ "guesses left.")
    #     print("Available letters: "+available_letters)
    #     hangman(secretWord)
    #     num_of_guesses -= 1
    #     print(br)
    #isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
    print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))

if __name__ == "__main__":
    main()


