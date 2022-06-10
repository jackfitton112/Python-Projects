#Title: Fizz Buzz MK1
#File: isimple.py
#Date created: 10/06/2022

#sets a loop that will count from 0 - 50
for i in range(51):
    #checks if number is 0, as % 3 and %5 of 0 are both 0 but it should display 0 not fizzbuzz
    if i == 0:
        print("0")
    #uses % (modulus (Remainder)) to check if the number can cleanly be divided by 5 and 3
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    #checks if number is only cleanly divisavle by 3
    elif i % 3 == 0:
        print("Fizz")
        #checks if number is only cleanly divisavle by 5
    elif i % 5 == 0:
        print("Buzz")
    #prints the current number if non of the above conditions are true
    else:
        print(str(i))
