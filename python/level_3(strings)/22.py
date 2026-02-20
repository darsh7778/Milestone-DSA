# Check if a string is palindrome.

str = input("Enter a string : ")

if (str == str[::-1]):
    print("Palindrome")
else:
    print("not a palindrome")