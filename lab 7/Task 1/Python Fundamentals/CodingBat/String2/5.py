def end_other(a, b):
    a = a.lower()
    b = b.lower()
    
    if a.find(b) == len(a) - len(b):
        return True
    if b.find(a) == len(b) - len(a):
        return True
    
    return False