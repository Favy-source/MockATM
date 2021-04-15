def operation(first,second,operator):

    if(operator == 1):
        return first + second
    if(operator == 2):
        return first - second
    if(operator == 3):
        return first / second
    if(operator == 4):
        return first * second

    return "invalid selection or input"  



print("Welcome to calc.py, please enter 2 values to perform an operation")
firstValue = float(input("Input the first value? \n"))
secondValue = float(input("Input the second value? \n"))

print("Available operations")
print("1. sub - subtract two numbers")
print("2. add - add two numbers")
print("3. mul - multiply two numbers")
print("4. div - divide two numbers")

operator = int(input("Which of the above would you like to perform? \n"))


print(operation(firstValue,secondValue,operator))


