string = input("Enter a string:")
init_vowel = 0
vowel = 'aeiouAEIOU'
for str in string:
    if str in vowel:
        init_vowel+=1
print("Number of vowels:",init_vowel)
