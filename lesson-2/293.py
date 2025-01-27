A = input("Write something: ")
B = ''.join(char for char in A if char not in " ")
print(B)