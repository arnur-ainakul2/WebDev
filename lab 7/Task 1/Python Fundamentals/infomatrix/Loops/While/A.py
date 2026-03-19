import math
a=int(input())
while a>0:
    if math.sqrt(a).is_integer():
        print(a)
    a-=1

