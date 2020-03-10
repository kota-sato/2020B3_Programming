import sys
import random
args = sys.argv

for word in args[1:]:
    if len(word) <= 3:
        print(word, end=' ')
    else:
        tmp_sr = word[1:len(word)-1]

        sr = ''.join(random.sample(tmp_sr, len(tmp_sr)))
        print(word[0] + sr + word[-1], end=' ')

