# 50.	Print Floyd’s triangle (numbers).
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num =num+ 1
    print()