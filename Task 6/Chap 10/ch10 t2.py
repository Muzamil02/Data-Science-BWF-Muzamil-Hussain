#Exercise 10.2

file_path = ('E:\Bytewise Fellowship\Task 6\Chap 10\learning_python.txt')
with open(file_path, 'r') as file:
    for line in file:
        modified_line = line.replace('Python', 'C')
        print(modified_line.strip())