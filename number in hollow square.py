a = int(input())
b = int(input())
num = a 
for i in range(b):
    for j in range(b):
        if i == 0 or i == b -1 or j == 0 or j == b - 1 :
            print(num, end=" ")
        else:
            print(" ",end=" ")
        num += 1 
    print()
