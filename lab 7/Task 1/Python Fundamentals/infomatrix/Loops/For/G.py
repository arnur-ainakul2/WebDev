import math
a=int(input())
for i in range(1,math.ceil(math.sqrt(a)),1):
    if a%i==0 and i!=1:
        print(i)