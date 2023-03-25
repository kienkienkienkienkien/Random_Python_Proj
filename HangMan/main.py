from random import randint
import re
from re import search
import wordpool

if __name__ == "__main__":

    invalid = "invalid input"
    alp = "abcdefghijklmopqrstuvwxyz"

    def restart():
        prompt = ("\nDo u want to play again?\n(1) Yes\n(2) No\ninput: ")
        inp = input(prompt)
        if inp == "1":
            word_generating()
        elif inp == "2":
            print("thanks for1 playing")
        else: 
            print(invalid)


    def win(word, live):
        print("You Win!!! The word is: {}, and u beat it with {} live(s)".format(word, live))
        restart()
        
        
    def lose(word):
        print("You Lose!!!, the word is: ", word)
        restart()
        

    def guess_word(word, live, inpValid):
        guess = input(" \nguess word: ")
        if guess == "1":
            guess_letter(word, live, inpValid, mysWord)
        else: 
            if len(guess) != len(word):
                print("message: ", invalid)
                return inpValid, live
            else: 
                if guess == word:
                    inpValid = False
                    win(word, live)
                    return inpValid, live
                elif guess != word:
                    if guess in guessedWord:
                        print("u have alreay guess ", guess)
                        return inpValid, live
                    else:
                        if live > 1:
                            live -= 1
                            guessedWord.append(guess)
                            return inpValid, live
                            
                        elif live == 1 or live == 0: 
                            inpValid = False
                            lose(word)
                            return inpValid, live

    def guess_letter(word, live, inpValid, mysWord):
        guess = input("\nguess letter: ")
        letterPosList = []
        if guess == "1":
            guessOutp = guess_word(word, live,  inpValid)
            inpValid = guessOutp[0]
            live = guessOutp[1]

            return inpValid, live
        else: 
            if len(guess) != 1:
                print("message: ", invalid)
                return inpValid, live
            else: 
                letterPos = -1

                for match in re.finditer(guess, word):
                    letterPos = match.start()
                    letterPosList.append(letterPos)
                
                lenLetterPos = len(letterPosList)
                if lenLetterPos == 0:
                    if guess in guessedWord:
                        print("u have already guess",guess)
                        return inpValid, live
                    else:
                        if live > 1:
                            live -= 1
                            guessedWord.append(guess)

                            return inpValid, live
                        elif live == 1 or live == 0: 
                            inpValid = False
                            lose(word)
                            return inpValid, live
                else:
                    for letterPos in letterPosList:
                        mysWord[letterPos] = guess
                    wordCheck = ("".join(mysWord))
                    if wordCheck == word:
                        inpValid = False
                        win(word, live)
                        return inpValid, live
                    else: 
                        return inpValid, live

    def guessing_word(word, inpValid, live, mysWord):
        print("\npress (1) to switch word/letter")
        print("word length: ", len(word))
        while inpValid:
            if len(guessedWord) > 0: 
                guessedWordList = ",".join(guessedWord)
                print("word/letter u have guessed: ",guessedWordList)
            if live == 0:
                inpValid = False
                lose(word)
            else: 
                print("\nlive: ", live)
                print(' '.join(mysWord))
            
                guessOutp = guess_letter(word, live, inpValid, mysWord)
                inpValid = guessOutp[0]
                live = guessOutp[1]

    def word_generating():
        global word, inpValid, live, mysWord, guessedWord
        pool = wordpool.words
        poolLen = len(pool)
        word = pool[randint(0,(poolLen - 1))]
        
        guessedWord = []

        mysWord = []
        for letter in word:
            mysWord.append("_")
        live = 7
        inpValid = True

        guessing_word(word, inpValid, live, mysWord)
        
    def main():
        print("This is shit Hangman")
        print("Theme: Country")
        prompt = """(1) Start \n(2) Exit \ninput: """
        inpValid = True
        while inpValid: 
            inp = input(prompt) 
            if inp == "1":
                word_generating()
                inpValid = False
            elif inp == "2":
                print("Thanks for playing, Bye!")
            else: 
                print("message: ", invalid)
    main()