s = input()
s_c = s[0]
for index in range(1, len(s)):
    if ord(s[index]) < ord(s_c):
        s_c = s[index]
print(s_c)
