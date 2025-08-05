def lot(a,b,c):
    if a>=b and a>=c:
        print(f"{a} is largest of three.")

    elif b>=a and b>=c:
        print(f"{b} is largest of three.")

    else:
         print(f"{c} is largest of three.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
lot(num1,num2,num3)

#FUNCTIONS