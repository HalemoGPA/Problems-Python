word_dict={"bed","bath","bedbath","and","beyond"}
wordsequence="bedbathandbeyond"
first_words_list=[];re1=[];just=[];newlist=[]
for i in range(len(wordsequence)):
    for j in range (i+1,len(wordsequence)+1):
        first_words_list.append(wordsequence[i:j])
for i in first_words_list:
    if i in word_dict:
        newlist.append(i)
for i in range (len(wordsequence)):
    just.append(wordsequence[0:i])
for j in just:
    if j in word_dict:
        re1.append(j)
for i in re1:
    if i in newlist:
        x=newlist.index(i)
        newlist.remove(i)
        print(newlist)
        newlist.insert(x,i)
