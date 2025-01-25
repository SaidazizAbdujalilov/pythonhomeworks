A = input("Write something: ")
B = A.strip()
C = ''.join(char for char in B if char in " ")
D = len(C)+1
print(f"there are {D} words in your sentence")