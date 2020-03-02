org_str = 'パタトクカシーー'
str2 = ''
str1 = ''

for i in range(0, 8):
    if i % 2 == 0:
        str2 += org_str[i:i+1]
    else:
        str1 += org_str[i:i+1]

print(str2)
print(str1)