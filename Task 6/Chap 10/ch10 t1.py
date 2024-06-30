#Exercise 10.1

file_path = ('E:\Bytewise Fellowship\Task 6\Chap 10\learning_python.txt')
with open(file_path, 'r') as file:
    content = file.read()
print("Reading the entire file:\n")
print(content)

print("Looping over the file object:\n")
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())

print("\nStoring lines in a list and working with them outside the 'with' block:\n")
with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())