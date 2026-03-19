a=int(input())
ispow=True
while ispow:
    if a==1:
        ispow=True
        break
    if a%2==0:
        a=a/2
        ispow=True
    else:
        ispow=False
if ispow:
    print("YES")
else:
    print("NO")
        