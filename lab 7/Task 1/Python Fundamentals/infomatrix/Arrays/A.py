import math
arr=[]
n=int(input())
for i in range(n):
    a=int(input())
    if i%2==0:
        arr.append(a)
for i in range(len(arr)):
    print(arr[i],end=" ")
