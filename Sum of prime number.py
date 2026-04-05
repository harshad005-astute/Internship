a = int(input())
b = int(input())

sum_p_num = 0 
for i in range(a, b+1):
    if i > 1:
        prime = True 
        for j in range(2, int(i**0.5)+1):
            if i %j ==0:
                prime = False
                break
        if prime :
            sum_p_num += i 
print(sum_p_num)
