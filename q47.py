# 47.	Print a full pyramid of *.
for i in range(1, 6):  
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()