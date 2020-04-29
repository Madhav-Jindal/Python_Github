maximum=None
smallest=None
while True:

    n=input("Enter Number")
    if n=="done":
        break
    try:
        fn=int(n)
    except:
        print("Invalid input")
        continue
    if maximum is None:
        maximum=fn
    elif fn>maximum :
        maximum=fn
    if smallest is None:
        smallest=fn
    elif fn<smallest :
        smallest=fn

print("Maximum is",maximum)
print("Minimum is",smallest)
