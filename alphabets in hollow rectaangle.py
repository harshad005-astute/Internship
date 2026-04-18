rows = int(input())
cols = int(input())

space = 2 * cols - 3 
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
curr_index = 0 
for row in range(rows):
    each_row = ""
    
    for col in range(cols):
        if row == 0 or row == rows -1:
            each_row = each_row + alphabet[curr_index] + " "
        elif col == 0:
            each_row = each_row + alphabet[curr_index] +" "* space +alphabet[cols + curr_index - 1]
        curr_index = curr_index + 1 
    print(each_row)
