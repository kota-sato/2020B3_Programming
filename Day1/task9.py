import sys
import random
args = sys.argv



for i in range(1, len(args)):
    if len(args[i]) <= 3:
        print(args[i]),
    else :
        tmp_sr = (args[i])[1:len(args[i])-1]

        sr = ''.join(random.sample(tmp_sr, len(tmp_sr)))
        print(((args[i])[0:1]) + sr + ((args[i])[len(args[i])-1:len(args[i])])),

