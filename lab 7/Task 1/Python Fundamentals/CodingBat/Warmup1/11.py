def front_back(str):
  if len(str) <= 1:
    return str

  s=""
  s=s+str[-1]
  s=s+str[1:len(str)-1]
  s=s+str[0]
  return s
  
