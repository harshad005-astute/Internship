n = int(input())
h_s = "  "*(n-2)
for row in range(n):
    if row == 0 or row == n - 1:
        each_row = "* "*n 
    else:
        each_row = "* " + h_s +"*"
    print(each_row)
    
l_s = "  "*(n - 1)
for row in range(1, n):
    if row == n - 1:
        each_row = "* "*n 
    else:
        each_row = l_s +"*"
    print(each_row)
