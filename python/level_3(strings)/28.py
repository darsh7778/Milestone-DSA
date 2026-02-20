# Check if string contains only digits. 

s = input("enter something : ")

is_digit = True

for ch in s:
    if ch < '0' or ch > '9':
        is_digit = False
        break

print(is_digit)

