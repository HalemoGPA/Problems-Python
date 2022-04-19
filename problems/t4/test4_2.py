T=[(30,75),(0,50),(60,150),(80,150),(20,40),(19,35)]
numlist=[]
x=max(T[:]);y=max(x)
z=min(T[:]);q=min(z)
nums=range(q,y)
for tuple in T :
    for x in range(tuple[0],tuple[1]):
        if x in nums :
            numlist.append(x)
dup_dict={}
for i in numlist:
    dup_dict[i]=numlist.count(i)
maxi=0
for k,v in dup_dict.items():
    if v >maxi:
        maxi=v
print(maxi)
