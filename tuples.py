#Print 10 most occuring words froma file
hndl=open("romeo.txt")
count=dict()
word=list()
for i in hndl:
    word=i.split()
    for j in word:
        count[j]=count.get(j,0)+1

temp=list()
for key,value in count.items():
    temp.append([value,key])
temp=sorted(temp,reverse=True)
print(temp[:10])