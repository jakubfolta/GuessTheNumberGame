def digit_sum(n): #Define function which will add digits of a positive number
  total = 0 #Set variable to 0
  if n >= 0: #Check if number is greater than or equal to 0
    for x in str(n): #Loop by converted to a string number
      total += int(x) #Add and set to variable converted to integer digits of a number 
    print (total) #Print added digits to console
  else: #If number is negative print a hint about positive number
    print ('Positive number please')

digit_sum(134) #Call to function



    
def digit_su(num): # Defining function which will add digits of a positive number
  if num >= 0:
    print (sum(int(a) for a in str(num)))
  else:
    print ('Positive number please.')
    
digit_su(-435)




def digit_sum(n): # Defining function which will add digits of a positive number
  su = [0]
  if n >= 0:
    for x in str(n):
      su.append(int(x))
    print (sum(su))
  else:
    print ('Positive number please.')
  
digit_sum(134)

    


