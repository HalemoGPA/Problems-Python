substring=input("Enter a substring : ")
k=int(input("Enter the maximum different letters in the substring : "))
newlist=[]
sublist=[]
final_list=[]
for i in range(len(substring)):
    for j in range(i+1,len(substring)+1):
        sublist.append(substring[i:j])
for w in sublist:
    if len(set(list(w)))<=k:
        newlist.append(w)
longest_string=max(newlist,key=len)
for y in newlist:
    if len(y)==len(longest_string):
        final_list.append(y)
for l in final_list:
    print(l,end=" ")
