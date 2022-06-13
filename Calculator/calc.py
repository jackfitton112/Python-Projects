#Title: Python Calculator
#File: calc.py
#Date created: 13/06/2022



def add(number1,number2):
    total = int(number1) + int(number2)
    return total

def subtract(number1,number2):
    total = int(number1) - int(number2)
    return total

def multiply(number1,number2):
    total = int(number1) * int(number2)
    return total

def divide(number1,number2):
    total = int(number1) / int(number2)
    return total


calcTotal = 0

while True:
    print ("Current Total: "+str(calcTotal))
    option = input("""Select an option:\n(+) Add\n(-) Minus\n(*) Multiply\n(/) Divide \n:""")

    number2 = input("\n"+str(calcTotal)+" "+str(option)+" :")

    if option == "+":
        number1 = calcTotal
        calcTotal = add(calcTotal, number2)
        print(str(number1)+" + "+str(number2)+ " = "+str(calcTotal))

    elif option == "-":
        number1 = calcTotal
        calcTotal = subtract(calcTotal, number2)
        print(str(number1)+" - "+str(number2) +" = "+str(calcTotal))

    elif option == "/":
        number1 = calcTotal
        calcTotal = divide(calcTotal, number2)
        print(str(number1)+" / "+str(number2) +" = "+str(calcTotal))

    elif option == "*":
        number1 = calcTotal
        calcTotal = multiply(calcTotal, number2)
        print(str(number1)+" * "+str(number2)+ " = "+str(calcTotal))
