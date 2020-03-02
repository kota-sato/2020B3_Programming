import sys
args = sys.argv
word_list = []
char_list = []
tmp_str = ''
bi_str = ''
num = 2

for i in range(1, len(args) - 1):
    tmp_list = []
    for j in range(0, num ):
        tmp_list.append(args[i +j])
    word_list.append(tmp_list)
    tmp_str += args[i]

print('word bi-gram:'),
print(word_list)

tmp_str += args[i+1]
for i in range(0, len(tmp_str) - 1):
    bi_str = ''
    tmp_list = []
    for j in range(0, num):
        bi_str += tmp_str[i + j]
    char_list.append(bi_str)

print('char bi-gram:'),
print(char_list)




