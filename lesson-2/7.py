A = input("Enter the integer:")
if A[len(A)-1] in "02468":
    print(f"{A} is even")
else:
    print(f"{A} is odd")