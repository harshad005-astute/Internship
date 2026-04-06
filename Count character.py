s = input()
n = int(input())
count = 0
for i in s:
    if ord(i) == n:
        count += 1
print(count)
