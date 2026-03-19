import math
arr=[]
n=int(input())
t=0
for i in range(n):
    a=int(input())
    arr.append(a)
for i in range(1,n-1,1):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        t=t+1
print(t)
