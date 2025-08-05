a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1  
min_num = a if a < b else b
i = 1
while i <= min_num:
    if a % i == 0 and b % i == 0:
        gcd = i
    i += 1

max_num = a if a > b else b
while True:
    if max_num % a == 0 and max_num % b == 0:
        lcm = max_num
        break
    max_num += 1

print(f"GCD of {a} and {b} is:",gcd)
print(f"LCM of {a} and {b} is:",lcm)


#REDO 