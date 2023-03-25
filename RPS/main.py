from random import randint
def play(playerInp):
    draw = "Draw!"
    win = "You Win!"
    lose = "You Lose!"
    invalid = "Invalid Input"

    t = ["Rock", "Paper", "Scissor"]
    computerInp = t[randint(0,2)]

    print("computer play: ", computerInp)
    

    if playerInp == "r": playerInp = "Rock"
    if playerInp == "p": playerInp = "Paper"
    if playerInp == "s": playerInp = "Scissor"


    if playerInp == computerInp: return draw
    elif playerInp == "Rock" and computerInp == "Paper": return lose
    elif playerInp == "Rock" and computerInp == "Scissor": return win
    elif playerInp == "Paper" and computerInp == "Rock": return win
    elif playerInp == "Paper" and computerInp == "Scissor": return lose
    elif playerInp == "Scissor" and computerInp == "Rock": return lose
    elif playerInp == "Scissor" and computerInp == "Paper": return win
    else: return invalid
        
    

def main():
    prompt = """
    Rock, Paper, Scissor
    to exit type: end """
    print(prompt)

    player = True
    while player: 
        playerInp = input("(R)ock, (P)aper, (S)cissor: ")
        if playerInp  == "end":
            print("thanks for playing lmao!")
            player = False
        print(play(playerInp))

main()