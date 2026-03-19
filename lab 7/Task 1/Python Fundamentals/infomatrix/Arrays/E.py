import math
arr=[]
n=int(input())
pair=False
for i in range(n):
    a=int(input())
    arr.append(a)
for i in range(n-1):
    if arr[i]>0 and arr[i+1]>0:
        pair=True
        break
    elif arr[i]<0 and arr[i+1]<0:
        pair=True
        break
if pair:
    print("YES")
else:
    print("NO")
