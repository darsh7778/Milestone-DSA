#Calculate simple interest

principal = int(input("enter the principal amount => "))
rate = int(input("enter the rate of interest => "))
time = int(input("enter the time in months => "))

interst = principal * rate * time / 100

print(f"the interest of {principal} is {interst}")

