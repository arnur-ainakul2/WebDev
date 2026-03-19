def pos_neg(a, b, negative):
  if negative==True:
    if a<0 and b<0:
      return True
    else:
      return False
  if negative==False:
    if a<0 and b>0:
      return True
    if a>0 and b<0:
      return True
    if a<0 and b<0:
      return False
    if a>0 and b>0:
      return False
  
