from random import randint
import re
from re import search
import wordpool

def compare_words(guessLetterPos, wordList):
    
    
    print(guessLetterPos[0][1])
    #print(wordList)

def guess_word(wordList):
    guessValid = True
    guessTime = 1
    guessLetterPos = []
    letterNpos = []

    while guessValid:
        if guessTime <= 5: 
            #prompt = "Guess {}: ".format(guessTime)
            #guessInp = input(prompt)
            guessInp = "falls"
            if len(guessInp) != 5: 
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
        else: 
            guessValid = False

def generate_word():
    global wordList, rightLetter

    pool = wordpool.words
    poolLen = len(pool)
    word = pool[randint(0,(poolLen - 1))]

    
    wordList = []
    rightLetter = []
    for letter in word:
        wordList.append(letter)

    print(wordList)
    guess_word(wordList)
    
def main():
    print("Welcome to shit worlde!!")
    generate_word()

main()