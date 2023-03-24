live = 7
word = "bald"
len = len(word)
mysWord = []

for x in word:
    mysWord.append("_")

print(mysWord)
guess = True
while guess == True: 
    inp = input("inp: ")
    
    if inp in word:
        index = word.index(inp)
        mysWord[index] = inp
        print(mysWord)
    else: 
        live -= 1
        print("wrong, live: ", live)
        guess = False
    if inp == word:
        print("you win!")
        guess = False
        

