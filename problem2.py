name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)

print("Name has been saved successfully.")