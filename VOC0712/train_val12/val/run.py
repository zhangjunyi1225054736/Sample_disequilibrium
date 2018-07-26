import glob
a  = glob.glob("./*.txt")

for i in range (len(a)):
    file = open(a[i])
    s = a[i].split("/")[-1].strip()
    f = open("number","a") 
    f.write(s+"  "+str(len(file.readlines()))+"\n")
        
