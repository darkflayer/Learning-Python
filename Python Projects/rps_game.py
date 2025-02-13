# below is the rock paper scissors game 
import random
def get_choice():
    player_choice=input("Enter a choice rock,paper and scissor: ")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

#function to check who is the winner
def check_win(player,computer):
    print(f"You chose {player},Computer chose {computer}")
    if(player==computer):
        print("Its a tie !")
    elif(player=="rock"):
        if(computer=="paper"):
            print("Paper wraps Rocks,You lose.")
        else:
            print("Rock smashes Scissor,You Won!")
    elif(player=="paper"):
        if(computer=="rock"):
            print("Paper wraps Rocks,You Won!.")
        else:
            print("Scissor cuts paper,You lose.")
    elif(player=="scissors"):
        if(computer=="paper"):
            print("Scissor cuts paper,You Won!")
        else:
            print("Rock smashes Scissor,You lose.")
    
choices=get_choice()
result=check_win(choices["player"],choices["computer"])
print(result)