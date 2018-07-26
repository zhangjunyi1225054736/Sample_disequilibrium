#file = open("./list")
#a = [line.strip() for line in  file.readlines()]

import glob
b = glob.glob("./*.txt")
#count = 0
#r = [[]for i in range (20)]

'''
for filename in b:
    s = filename.split("/")[-1].strip()
    f = open(s)
    r[count] = [line.strip() for line in  f.readlines()]
    count  = count + 1
'''

for n in range(1):
    for m in b:
        s = m.split("/")[-1].strip()
        f = open(s)
        print f.readline()
