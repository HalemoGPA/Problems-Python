#This program is for counting how many letters in a file
def count_letters() :
    fname=input('Enter file name : ')
    if len(fname) < 1 : fname="file.txt"
    handle = open(fname)
    lista=list()
    zz=""
    for line in handle :
        line.rstrip()
        x=line.split()
        for word in x :
            lista.append(word)
    for i in lista :
        for l in i :
            zz=zz+l
    print("The number of letters is : ",len(zz))
while True :
    count_letters()
