hndl=open("mbox-short.txt")
word=[]
count=dict()
fword=[]
inpos=0
for i in hndl:
    word=i.split()
    if i=='' or i=='\n':
        continue
    if word[0]=="From":
        inpos=i.find(':')
        fword.append((i[inpos-2:inpos]))
        
for j in fword:
    count[j]=count.get(j,0)+1

temp=list()
for k,v in count.items():
    temp.append((k,v))
temp=sorted(temp)
for k,v in temp:
    print(k,v)
    