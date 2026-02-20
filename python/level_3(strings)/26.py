# Capitalize first letter of each word

str = input("enter a string : ")

print(str.title())

# or we use

print(str.capitalize())

# or we use (logic)

words = str.split()
capitalized = []

for word in words:
    capitalized.append(word.capitalize())
    
result = " ".join(capitalized)

print(result)
