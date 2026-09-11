def greet(name):
    print(f"Hello {name}. Welcome to my program.")

try:
    your_name = input("Enter your name: ")

    if not your_name.isalpha():
        raise ValueError("Invalid name")

    greet(your_name)

except ValueError:
    print("Sorry, you entered an invalid name.")