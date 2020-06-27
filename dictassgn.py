hndl=open("mbox-short.txt")
name=list()
w=list()
for i in hndl:
    i=i.rstrip()                      
    w=i.split()                
    if i=='':                  
        continue
    if w[0]=="From":
         name.append(w[1])           

final=dict()
for j in name:
    final[j]=final.get(j,0)+1

maxw=None
maxc=None
for k,v in final.items():
    if maxc==None or v>maxc:
        maxw=k
        maxc=v
print(maxw,maxc)