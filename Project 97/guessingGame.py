import random
print("This is a number guessing game")
gameNumber=random.randint(1,9)
chances=0
while chances < 5:
    guess=int(input("enter your guess"))
    if(gameNumber==guess):
        print("Congratulations you won")
        break
    elif(guess < gameNumber):
        print("Your guess was too low.Guess a number higher than",guess)
    else:
        print("Your Guess was too high.Guess a number less than",guess)   
    chances+=1
if not chances < 5:
    print("You lose. try again.the number is", gameNumber)
