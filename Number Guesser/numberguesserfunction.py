#Title: Number Guesser MK 2
#File: numberguesserfunction.py
#Date created: 10/06/2022


#imports random libary for use generating random number
from random import randint

#defines a function as guess, to be called in the super loop
def guess(input, number):

    #uses if and elif statements to check if the guess is correct or higher or lower than the number
    if input == number:
        return "\nYou got it, the number was: "+ str(number)

    elif input > number:
        return "\nGuess too high, try again"

    elif input < number:
        return "\nGuess too low, try again"





print ("Guess a number between 0 - 100\n")

#sets "number" to a random int between 0 - 100
number = randint(0,100)

#number of guesses is defined as a var
i = 5

# gives the user 5 guesses
while i != 0:

    #gets the users input and stores it as a userGuess
    userGuess = int(input("\nGuess: "))


    #prints the output of function guess with the vars userGuess and number
    print(guess(userGuess, number))


    if userGuess != number and i > 0:
        i -= 1
        print ("\nyou have "+str(i)+" guesses remaining")
    elif i == 0:
        print ("\nyou have ran out of guesses! try again")
        break
    else:
        break
