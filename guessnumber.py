import random

def guess_the_number(name=input("What is your name?:")):
    secretNr=random.randint(1,10)
    print("Dear {}, I am thinking of a number between 1 and 10, can you guess it? You have 5 tries.".format(name))
    for guessNr in range (1,5):
        guess=int(input())
        if guess<secretNr:
            print("Guessed nr is too low")
        elif guess>secretNr:
            print("Guessed nr is too high")
        else:
            break

    if guess==secretNr:
        print("You have guessed the correct number")
    else:
        print("Number of tries surpassed, the number I was thinking of is {}.". format(secretNr))


guess_the_number()