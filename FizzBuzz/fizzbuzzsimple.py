#Title: Fizz Buzz MK1
#File: isimple.py
#Date created: 10/06/2022


for i in range(51):
    if i == 0:
        print("0")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(str(i))
