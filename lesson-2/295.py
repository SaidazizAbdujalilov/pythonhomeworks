A = input("Write your company name: ")
B = A.split()
C = ''.join(word[0].upper() for word in B)
print(C)
