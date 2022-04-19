fname=input('enter file name : ')
handle=open (fname)
lis=list()
for line in handle:
    line=line.rstrip()
    words=line.split()
    for word in words :
        lis.append(word)
print(len(lis))        
