fhndl=open("romeo.txt")
ls=list()
ls1=list()
for i in fhndl:
    i=i.rstrip()
    ls=i.split()
    for j in ls:
        if j not in ls1:
            ls1.append(j)

ls1.sort()
print(ls1)