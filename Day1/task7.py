
org_str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
new_str = ''

for i in range(0, len(org_str)):
    if org_str[i:i+1] == ',' or org_str[i:i+1] == '.':
        pass
    else:
        new_str += org_str[i:i+1]

mylist = new_str.split()
new_mylist = [len(mylist[i]) for i in range(0, len(mylist))]

print(new_mylist)