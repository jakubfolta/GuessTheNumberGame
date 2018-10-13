def digit_sum(n):
  total = 0
  if n >= 0:
    for x in str(n):
      total += int(x)
    print (total)
  else:
    print ('Positive number please')

digit_sum(134)



    
def digit_su(num):
  if num >= 0:
    print (sum(int(a) for a in str(num)))
  else:
    print ('Positive number please.')
    
digit_su(-435)




def digit_sum(n):
  su = [0]
  if n >= 0:
    for x in str(n):
      su.append(int(x))
    print (sum(su))
  else:
    print ('Positive number please.')
  
digit_sum(134)

    


