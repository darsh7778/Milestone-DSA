# Check if two strings are anagrams 

s1 = "Listen"
s2 = "Silent"

str_1 = s1.lower()
str_2 = s2.lower()

if sorted(str_1) == sorted(str_2):
    print("both are Anagrams")
else:
    print("not a Anagrams")
