#Title: Password Generator
#File: passwordgen.py
#Date created: 10/06/2022


#imports libs required
import random
from random import randint
import string
import datetime


#the generate function takes a length and charset and returns a password
def generate(length, charset):
    password = []
    for i in range(length):
        if i % randint(1,length) == 0:
            letter = random.choice(charset)
            letter = letter.upper()
            if letter.isdigit == True:
                letter = str(letter)
            password.append(letter)
        else:
            password.append(random.choice(charset))
    return password

#these functions set the charset for generate and pass them to it.
def mixedchars(length):
    chars = list(string.ascii_letters)
    random.shuffle(chars)
    return generate(length, chars)

def mixedcharsandnums(length):
    chars = list(string.ascii_letters + string.digits)
    random.shuffle(chars)
    return generate(length, chars)


def specialchars(length):
    chars = list(string.ascii_letters + string.digits + "!£$%^&*()[]{},.-+=")
    random.shuffle(chars)
    return generate(length, chars)

#used for the selectors, calls the required function depending on input
def selector(Input,length):
    if Input == 1:
        return mixedchars(length)
    elif Input == 2:
        return mixedcharsandnums(length)
    elif Input == 3:
        return specialchars(length)
    else:
        return "Please enter a valid selection"

#used for saving the password to a file
def savepassword(password):
    x = datetime.datetime.now()
    f = open("password.txt", "a")
    f.write("\n")
    f.write("["+str(x)+"]"+''.join(password))
    f.close()
    return


print("""
      _____                                    _    _____                           _
     |  __ \                                  | |  / ____|                         | |
     | |__) |_ _ ___ _____      _____  _ __ __| | | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __
     |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
     | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |
     |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|

    \nBy Jack Fitton """)

while True:

    print("Please select one of the following options:\n1.Mixed case letters (AbCDefGH)\n2.Mixed case letters and numbers (A4b5c8F)\n3.Mixed case letters, numbers and special characters (A!1b4$c)")

    selection = int(input("\nPick an option (1, 2 or 3): "))
    if selection <= 3 and selection != 0:
        length = int(input("Pick the length of your password: "))

        passwordout = selector(selection, length)
        print ("\n\nYour password is: ")

        print (''.join(passwordout))

        save = input("\nWould you like to save this file? Y/N: ")
        save = save.upper()

        if save == "Y":
            print ("Saving password.txt...")
            savepassword(passwordout)
            print("\n\nPassword has been saved")
            break
        else:
            print("Thank you for using this service!")
            break

    else:
        print("\n**Please enter a valid selection**\n\n")
