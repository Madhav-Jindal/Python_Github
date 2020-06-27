hndl=open("mbox-short.txt")
count=dict()
for i in hndl:
    word=i.split()
    for c in word:
        count[c]=count.get(c,0)+1



max=None
maxc=None
for k,v in count.items():
    if maxc is None or v > maxc :
        max=k
        maxc=v
print(max,maxc)
