# Count vowels and consonants

str = input("enter the string : ")

vowel = ['a' , 'e' , 'i' , 'o' , 'u']

count_vowel = 0
count_consonant = 0

for ch in str:
    if ch.lower() in vowel:
        count_vowel+=1
    else:
        count_consonant+=1

print("vowel :", count_vowel)
print("consonant :", count_consonant)

