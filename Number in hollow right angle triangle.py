a = int(input())
b = int(input())
for row in range(1, b+1):
    i_s = "  "*(row - 1)
    
    if row == 1:
        F_r =""
        
        for column in range(b):
            F_r += str(a)+" "
            a += 1 
        print(i_s + F_r)
    
    elif row == b:
        l_r = str(a) +" "
        print(i_s + l_r)
        
    else:
        each_row = str(a)+" "
        h_s = "  "*(b - row - 1)
        each_row += h_s 
        a += 1 
        each_row += str(a) +" "
        a += 1 
        print(i_s+each_row)
            
