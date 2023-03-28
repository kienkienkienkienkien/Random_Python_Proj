from random import randint
import re
from re import search
import wordpool


def lose_message(word):
    message = "L, loser the word is {}". format(word)

    return message


def win_message(word):
    message = "Yayay, u won!!!, the word is {}". format(word)

    return message
def show_message(rightPosList, wrongPosList):
    if len(rightPosList) > 0:
        right = ", ".join(rightPosList)
        print("Correct Letter, Correct Position: {}".format(right))
    if len(wrongPosList) > 0:
        wrong = ", ".join(wrongPosList)
        print("Correct Letter, Wrong Position: {}".format(wrong))

def compare_words(guessLetterPos, wordList):
    
    count = 0
    lenList = len(guessLetterPos)
    rightPosList = []
    wrongPosList = []

    while count <= (lenList - 1):
        index = wordList.index(guessLetterPos[count][0])

        if index == guessLetterPos[count][1]:
            rightPosList.append(guessLetterPos[count][0])
        else: 
            wrongPosList.append(guessLetterPos[count][0])
        count +=1

    show_message(rightPosList, wrongPosList)

    #print(wordList)

def guess_word(wordList, word):
    global guessLetterPos, letterNpos
    guessValid = True
    guessTime = 1
    guessLetterPos = []
    letterNpos = []
    
    

    invalid = "invalid input, 5 letters only"

    while guessValid:
        if guessTime <= 5: 
            prompt = "\nGuess {}: ".format(guessTime)
            guessInp = input(prompt).lower()

            guessLetterPos.clear()
            letterNpos.clear()
            if len(guessInp) != 5: 
                print("message: ", invalid)
            elif guessInp == word:
                print(win_message(word))
                guessValid = False
            else: 
                count = 0
                for letter in guessInp:
                    #print("l: ", letter)
                    if letter in wordList:
                        letterNpos = [letter, count]
                        guessLetterPos.append(letterNpos) 
                    else:
                        pass
            
                    count += 1
                compare_words(guessLetterPos, wordList)  
                guessTime += 1
                if len(guessLetterPos) == 0:
                    print("lmeo, nothing is correct, L bozo")
                    
        else: 
            print(lose_message(word))
            guessValid = False

def generate_word():
    global wordList

    pool = wordpool.words
    poolLen = len(pool)
    word = pool[randint(0,(poolLen - 1))]

    
    wordList = []
  
    for letter in word:
        wordList.append(letter)

    guess_word(wordList, word)
    
def main():
    print("Welcome to shit worlde!!\n")
    generate_word()

main()