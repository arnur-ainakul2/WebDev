def count_hi(str):
  t=0
  for i in range(len(str)-1):
    if str[i]=='h' and str[i+1]=='i':
      t=t+1
  return t
      