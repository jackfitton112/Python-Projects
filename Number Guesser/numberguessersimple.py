#Title: Number Guesser MK 1
#File: numberguessersimple.py
#Date created: 10/06/2022


#imports random libary for use generating random number
from random import randint

print ("Guess a number between 0 - 100\n")

#sets "number" to a random int between 0 - 100
number = randint(0,100)

# sets a super loop so the user can have multiple guesses
while (True):

    #gets the users input and stores it as a userGuess
    userGuess = int(input("Guess: "))



    #uses if and elif statements to check if the guess is correct or higher or lower than the number
    if userGuess == number:
        print ("\nYou got it, the number was: "+ str(number))

    elif userGuess > number:
        print ("\nGuess too high, try again")

    elif userGuess < number:
        print ("\nGuess too low, try again")
