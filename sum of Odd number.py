a = int(input())
sum_odd = 0 
for i in range(1, a+1):
    if i%2 != 0:
        sum_odd += i 
print(sum_odd)
