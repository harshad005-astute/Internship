a = input()
result = ""
for ch in a:
    if ch in "aeiouAEIOU":
        continue
    result += ch 
print(result)
    
