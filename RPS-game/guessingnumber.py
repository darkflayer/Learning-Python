import random

secret_number=random.randint(1,100)
guess=None

print("Guess a number between 1 to 100")

while(guess!=secret_number):
    guess=int(input("Enter your Guess : "))
    if(guess<secret_number):
        print("Guessed too low!,Try higher value")
    elif(guess>secret_number):
        print("Guessed too high!,Try lower value")
    else:
        print("Cogratulations!! You Guessed it right")
