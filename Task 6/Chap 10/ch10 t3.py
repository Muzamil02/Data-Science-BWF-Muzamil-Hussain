#Exercise 10.3

name = input("Enter your name: ")
file_name = 'guest.txt'
with open(file_name, 'w') as file:
    file.write(name)
print(f"Successfully wrote '{name}' to '{file_name}'.")