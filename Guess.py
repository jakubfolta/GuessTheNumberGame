import random
import time

def guess():
  print('Please guess the number from 1 -20 in 5 guesses.')

  number = random.randint(1,20)

  for guessesTaken in range(5):
    guess = int(input('What\'s your guess? '))
    if guess < number:
      print('Your guess is too low.')
    elif guess > number:
      print('Your guess is too high.')
    elif guess == number:
      break

  guessesTaken = guessesTaken + 1
  if guess == number:
    print('Great, you guessed my number in', str(guessesTaken)+ ' guesses!')
  elif guess != number:
    print('Sorry, my number was', str(number)+ '.\nTry again!!!')

  print('Thanks for playing!')

answer = 'yes'
while answer == 'yes' or answer == 'y':
  guess()
  answer = input('Do you want to play again?\nyes/y ' )
  
if answer != 'yes' or answer != 'y':
    print('Thanks again for playing! Take care, and see you next time!')
time.sleep(2)
exit()
  




