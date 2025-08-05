num = int(input("Enter a number:"))
if num == 1:
    print("1 is neither prime nor composite.")

else:
  divisors = []
  
  for i in range(2,num//2 + 1):
     if num%i == 0:
      print(f"{num} is divisible by {i}")
      divisors.append(i)
  
  if len(divisors) == 0:
     print(f"{num} is a Prime number.")
  else:
     print(f"{num} is not a Prime number.")
