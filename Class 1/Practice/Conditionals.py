name = ""
age = 0
color = ""

def enter_values():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    color = input("Enter your favorite color: ")

enter_values()
print(f"Hello {name}. ")
if age > 45:
    print("It looks like you are over the hill")
elif age < 30:
    print("It is looks like you are young")
else:
    print("Who knows")
if color == "blue":
    print("That is Michael's favorite color")
elif color == "red":
    print("This is Taylor's favorite color")
else:
    print("I don't know that color")

