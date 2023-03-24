from random import randint
import wordpool

if __name__ == "__main__":

    invalid = "invalid input"
    win = "You Win!!!"
    lose = "You Lose!!!"
    wrong = "Nope"

    live = 7
    mysteryWordList = []
    def guess_word(word, live):
        guess = input("guess: ")
        
        if len(guess) != len(word):
            return "invalid"
        else: 
            if guess == word:
                return "win"
            else:
                live -= 1
                return live
        

    def guess_letter():
        pass
    def game_starting(word):
        if live == 0:
            print(lose)
        else: 
            print("\nlive: ", live)

            for letter in word:
                mysteryWordList.append("_")
            print(' '.join(mysteryWordList))
            
            prompt = """(1) Letter
(2) Word
input: """

            inpValid = True
            while inpValid: # change to if so it wont loop
                inp = input(prompt)
                if inp == "1":
                    guess_word(word, live)
                elif inp == "2":
                    guess_letter(word, live)
                else: 
                    print(invalid)  

        

    def word_generating():
        pool = wordpool.words
        poolLen = len(pool)
        word = pool[randint(0,(poolLen - 1))]

        game_starting(word)
        
    def main():
        print("This is shit Hangman")
        prompt = """(1) Start
(2) Exit
input: """
        inpValid = True
        while inpValid: 
            inp = input(prompt)
            if inp == "1":
                word_generating()
                inpValid = False
            elif inp == "2":
                print("Thanks for playing, Bye!")
            else: 
                print(invalid)
    main()