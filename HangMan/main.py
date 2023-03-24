from random import randint
import re
from re import search
import wordpool

if __name__ == "__main__":

    invalid = "invalid input"

    def win(word, live):
        print("You Win!!! The word is: {}, live: {}".format(word, live))
        return
        
    def lose(word):
        print("You Lose!!!, the word is: ", word)
        return

    def guess_word(word, live, inpValid):
        guess = input("guess: ")
    

        if len(guess) != len(word):
            print("message: ", invalid)
            return inpValid, live
        else: 
            if guess == word:
                inpValid = False
                win(word, live)
                return inpValid, live
            elif guess != word:
                if live > 1:
                    live -= 1
                    return inpValid, live
                elif live == 1 or live == 0: 
                    inpValid = False
                    lose(word)
                    return inpValid, live
                
    def guess_letter(word, live, inpValid, mysWord):
        guess = input("guess letter: ")
        letterPosList = []
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
                if live > 1:
                    live -= 1
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
        count = 0 
        while inpValid:
            if live == 0:
                inpValid = False
                lose()
            else: 
                print("\nlive: ", live)
                
                print(' '.join(mysWord))
            
                prompt = """(1) Word \n(2) Letter \ninput: """
                #inp = input(prompt)
                inp = "2"
                if inp == "1":
                    guessOutp = guess_word(word, live, inpValid)
                    inpValid = guessOutp[0]
                    live = guessOutp[1]

                elif inp == "2":
                    guessOutp = guess_letter(word, live, inpValid, mysWord)
                    inpValid = guessOutp[0]
                    live = guessOutp[1]

                else: print(invalid)
            count += 1

    def word_generating():
        global word, inpValid, live, mysWord
        pool = wordpool.words
        poolLen = len(pool)
        word = pool[randint(0,(poolLen - 1))]
        
        mysWord = []
        for letter in word:
            mysWord.append("_")
        live = 7
        inpValid = True

        print("word: ", word)
        guessing_word(word, inpValid, live, mysWord)
        
    def main():
        print("This is shit Hangman")
        prompt = """(1) Start \n(2) Exit \ninput: """
        inpValid = True
        while inpValid: 
            #inp = input(prompt)
            inp = "1"
            if inp == "1":
                word_generating()
                inpValid = False
            elif inp == "2":
                print("Thanks for playing, Bye!")
            else: 
                print(invalid)
    main()