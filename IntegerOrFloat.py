def is_int(x): #Check if number is integer or float
  if round(x) > x:
    return False
  elif round(-x) > -x:
    return False
  else:
    return True

print (is_int(-86.0423))
input()
