import glob
#a  = glob.glob("./*.txt")
#number_file = open("./number")

def add(name,num,max_num):
    add_number = max_num - num
    a = glob.glob("./*.txt")
    for f in a:
        #print "121"
        if name == str(f).strip().split(".")[1][1:]:
            #file_from = open("/home/zhangjunyi/VOC0712/Main07/balance/train/result/"+"unique_"+name+".txt")
            file_to = open("./result/"+name+".txt","a+")
            for i in range(add_number):
                  file_from = open("/home/zhangjunyi/VOC0712/Main12/balance/val/result/"+"unique_"+name+".txt")
                  result = file_from.readline()
                  file_to.write(result)      

number_file = open("./number")
vec = number_file.readlines()
number = [[]for _ in vec]
n = 0 

for i in vec:
    number[n] = int(i.strip().split()[1])
    n = n + 1

number.sort()

for s in vec:
    name = str(s.strip().split()[0])[:-4]
    num = int(s.strip().split()[1])
    print (name,num)
    add(name,num,int(number[len(number)-1]))


'''
for i in range (len(a)):
    file = open(a[i])
    s = a[i].split("/")[-1].strip()
    f = open("number","a") 
    f.write(s+"  "+str(len(file.readlines()))+"\n")
'''     
