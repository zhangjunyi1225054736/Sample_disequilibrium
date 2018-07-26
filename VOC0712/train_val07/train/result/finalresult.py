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
fopen = [[] for _ in range(20)]

i = 0
for m in b:
    s = m.split("/")[-1].strip()
    fopen[i] = open(s)
    i = i + 1

number_file = open("../number")
vec = number_file.readlines()
number = [[]for _ in vec]
n = 0 
for i in vec:
   number[n] = int(i.strip().split()[1])
   n = n + 1

number.sort()
print number[len(number)-1]

final = open("train","a+")

for n in range(number[len(number)-1]):
    j = 0
    for m in b:
        s = m.split("/")[-1].strip()
        final.write(fopen[j].readline().strip()+"\n")
        j = j + 1
