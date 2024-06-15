import random

rn = random.randint(1,50)
userGuess = 0
guesses = 0

while(userGuess != rn):
    userGuess = int(input("Enter your guess-> "))
    guesses += 1 
    if(userGuess == rn):
        print("Your guess is right!")
    else:
        if(userGuess>rn):
            print("You guessed large number")
        else:
            print("You guessed small number")
        print("you guessed wrong!")

print(f"You guessed the number is {guesses} guesses")
with open("./score.txt","r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("you have hiscore")
    with open("./score.txt", "w") as f:
        f.write(guesses)


