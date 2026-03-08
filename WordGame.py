#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for ch in word:
        if letter == ch:
            return True
    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    correct = word[spot]
    if letter == correct:
        return True
    else:
        return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    rating = "" 
    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot) == True:
            rating = rating + myLetter.upper()
        elif inWord(myLetter, word) == True:
            rating = rating + myLetter.lower()
        else:
            rating = rating + "-"
    return rating

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    number = 1
    while number <= 6:
        #User should get 6 guesses to guess
        valid = False
        while valid == False:
            guess = input("Make a guess: ")
            guess = guess.lower()
            if guess not in wordList:
                print("word not in list.")
                valid = False
            else:
                valid = True 
        rating = rateGuess(guess, todayWord)
        if rating == todayWord.upper():
            print("you got it in", number, "tries.")
            break
        print("The word was", todayWord)
        #Ask user for their guess
        #Give feedback using on their word:
        number = number + 1





if __name__ == '__main__':
  main()
