# Simple Calculator scripts

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("""Select operations:
      1. Add
      2. Subtract
      3. Multiply
      4. Divide""")

choice = input("Enter choice (1/2/3/4): ")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if choice == '1':
    print("The sum of the numbers is: ", add(number1, number2))

elif choice == '2':
    print("The difference of the numbers is: ", subtract(number1, number2))

elif choice == '3':
    print("The product of the numbers is: ", multiply(number1, number2))

elif choice == '4':
    print("The quotient of the numbers is: ", divide(number1, number2))

else:
    print("Invalid input")