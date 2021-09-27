num1 = input("What number would you like?")
num2 = input("What other number would you like?")

sum = int(num1) + int(num2)

prod = int(num1) * int(num2)

while (sum!= prod):
    print("Wow, thats really wrong!")
    num1 = input("Type another number.")
    num2 = input("Type a second number.")
    sum = int(num1) + int(num2)
    prod = int(num1) * int(num2)

print("Thats correct! Finally...")
