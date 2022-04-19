import re
numlist=list()
hand=open("1.txt")
for line in hand:
    line=line.rstrip()
    y=re.findall("-*[0-9]+",line)
    for num in y:
        num=float(num)
        numlist.append(num)
print(sum(numlist))
