org_str = 'Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. ' \
          'Arthur King Can. '
new_str = org_str.replace(".", "")
new_str = new_str.replace(",", "")

word_dict = {}

# for i in range(0, len(org_str)):
#    if org_str[i:i+1] == ',' or org_str[i:i+1] == '.':
#       pass
#   else:
#      new_str += org_str[i:i+1]

my_list = new_str.split()

for i, word in enumerate(my_list):
    i += 1
    if i == 1 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 15 or i == 16 or i == 19:
        word_dict[word[0]] = i
    else:
        word_dict[word[0:2]] = i

print(word_dict)
