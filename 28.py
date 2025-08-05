n = int(input("Enter a number: "))
print("\nFibonacci Series:")
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"\nFactorial of {n} is:", factorial)
