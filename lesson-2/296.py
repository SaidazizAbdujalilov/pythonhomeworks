A = input("Write something: ")
B = input("Write a character that you want to remove: ")
C = ''.join(char for char in A if char.lower() not in B)
print(C)