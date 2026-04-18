n = int(input())
l__s = "  "*(n - 1)

for row in range(2* n - 1):
    if row == 0 or row == n - 1 or row == 2 * n - 2:
        each_row = "* " *n
    else:
        each_row = l__s + "*"
    print(each_row)
