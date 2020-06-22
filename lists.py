fhndl=open("mbox-short.txt")
ls=list
for i in fhndl:
    i=i.rstrip()
    ls=i.split()
    if i=='':
        continue
    if ls[0]=="From":
        print(ls[1])