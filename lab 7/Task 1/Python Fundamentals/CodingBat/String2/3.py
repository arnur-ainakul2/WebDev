def cat_dog(str):
  a=0
  b=0
  for i in range(len(str)-2):
    if str[i:i+3]=="cat":
      a=a+1
    elif str[i:i+3]=="dog":
      b=b+1
  if a==b:
    return True
  else:
    return False
      