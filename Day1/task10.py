import sys
args = sys.argv
word_list = []
char_list = []
tmp_str = ''
bi_str = ''
num = 2


for i in range(1, len(args) - 1):
    tmp_list = args[i:i + num]
    word_list.append(tmp_list)

print('word bi-gram:', end=' ')
print(word_list)
tmp_str += ''.join(args[1:])

for i in range(0, len(tmp_str) - num + 1):
    char_list.append(tmp_str[i:i+num])

print('char bi-gram:', end=' '),
print(char_list)




