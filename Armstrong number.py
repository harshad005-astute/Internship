a = int(input())
for i in range(a):
    v = int(input())
    
    s = str(v)
    p = len(s)
    s_o_d = 0 
    
    for j in s:
        s_o_d = s_o_d + int(j)**p
    if s_o_d == v:
        print(v)
