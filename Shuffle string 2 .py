a = input().strip()
b = input().strip()
result = ""
length = len(a)
for i in range(length):
    if i % 2 == 0:
        result += a[i]
    else:
        result += b[i] 
print(result)
