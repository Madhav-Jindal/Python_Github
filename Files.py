fname=input("Enter file name")
fhandle=open(fname)
count =0
value=0
for i in fhandle:
    if i.startswith("X-DSPAM-Confidence:"):
        inpos=i.find(':')
        value=value+float(i[inpos+1:])
        count = count+1
    else:
        continue

print("Average spam confidence:",float(value/count))