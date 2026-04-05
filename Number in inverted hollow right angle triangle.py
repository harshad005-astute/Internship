a = int(input())
start_number = 1 
for row in range(1, a+1):
    if row == 1:
        first_row =""
        for column in range(a):
            first_row += str(start_number) + " "
            start_number += 1 
        print(first_row)
    elif row == a:
        last_row = str(start_number)
        print(last_row)
    else:
        each_row = str(start_number)+" "
        h_s = "  "*(a - row - 1)
        each_row += h_s 
        start_number += int(len(h_s)/2) + 1 
        each_row += str(start_number) + " "
        start_number += 1 
        print(each_row)
