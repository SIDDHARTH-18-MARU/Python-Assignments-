def pn(n):
    if n == 0:
        return 0
    pn(n - 1)
    print(n)

a = int(input("Enter the value of n: "))
pn(a)


#RECURSION