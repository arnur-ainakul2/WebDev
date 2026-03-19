def mini(a,b,c,d):
    arr=[]
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.append(d)
    t=a
    for i in range(len(arr)):
        if t>arr[i]:
            t=arr[i]
    return t
x=mini(1,2,3,4)
print(x)
    