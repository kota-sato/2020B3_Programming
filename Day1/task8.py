org_str = 'Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
new_str = ''
new_mylist = []
for i in range(0, len(org_str)):
    if org_str[i:i+1] == ',' or org_str[i:i+1] == '.':
        pass
    else:
        new_str += org_str[i:i+1]

mylist = new_str.split()

for i in range(1, len(mylist)+1):
    if i == 1 or i == 5or i == 6 or i == 7or i == 8or i == 9 or i == 15or i == 16 or i == 19:
        tmp_str = (mylist[i-1])[0:1] + ':' + str(i)
        new_mylist.append(tmp_str)
    else:
        tmp_str = (mylist[i-1])[0:2] + ':' + str(i)
        new_mylist.append(tmp_str)

print(new_mylist)