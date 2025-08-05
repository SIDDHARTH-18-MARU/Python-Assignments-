while True:
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    add = x + y
    subtract = x - y
    multiply = x * y
    divi = x / y
    print("Addition = ",add)
    print("Subtraction = ",subtract)
    print("Multiplication = ",multiply)
    print("Division = ",divi)
    choice = input("Do you want to continue? (yes/no): ")
    if choice!='yes':
        break
print("Exiting!!")
