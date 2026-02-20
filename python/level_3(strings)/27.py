# Find longest word in a sentence 

sentense = input("write the sentense -> ")

words = sentense.split()
longest_word = max(words, key=len)

print("Longest word = ",longest_word)


# method 2 using loop 

sentense = input("write the sentense : ")

words = sentense.split()
longest_word = " "

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
        
print("longest word is", longest_word)

