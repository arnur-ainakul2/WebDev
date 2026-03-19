import math
arr=[]
n=int(input())
t=0
for i in range(n):
    a=int(input())
    arr.append(a)
for i in range(int(n/2)):
    buf=arr[i]
    arr[i]=arr[n-1-i]
    arr[n-1-i]=buf
for i in range(n):
    print(arr[i],end=" ")

