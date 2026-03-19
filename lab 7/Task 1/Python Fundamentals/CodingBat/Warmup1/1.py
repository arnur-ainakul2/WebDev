def sleep_in(weekday, vacation):
  if weekday==False and vacation==False:
    return True
  if weekday==True and vacation==False:
    return False
  if vacation==True and weekday==False:
    return True
  if weekday==True and vacation==True:
    return True