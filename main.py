# convert text to UPPERCASE function

def upper():
    text = input("YOUR TEXT: ")
    print(text.upper())

# convert text to lowercase function

def lower():
    text = input("your text: ")
    print(text.lower())

# convert text to Capitalize function

def capitalize():
    text = input("Your text: ")
    print(text.capitalize())

# convert text to Title function

def title():
    text = input("Your Text: ")
    print(text.title())

# interface

print("1. UPPERCASE\n2. lowercase\n3. Capitalize\n4. Title")
command = int(input("Choose: "))

match command:
    case 1:
        upper()
    case 2:
        lower()
    case 3:
        capitalize()
    case 4:
        title()
    case _:
        print("Wrong option!")