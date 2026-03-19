import math
def xor(a,b):
    if a==True and b==False:
        return True
    if a==False and b==True:
        return True
a=int(input())
b=int(input())
print(xor(a,b))