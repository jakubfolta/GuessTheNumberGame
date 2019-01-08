#This will be a "Guess the number" game.

import random
import time

guessesTaken = 0

print ('Hi there! In a sec you will play with me in a "Guess the number" game. \
I will choose some number beetwen 1 and 20 and you will have \
6 chances to guess my number.\nPlease tell me your name.')
name = input()
print ('\nNice to meet you', name + '!')

randomNumber = random.randint(1,20)
print ('\nSo, please tell me what number I am thinking about right now beetwen \
1 and 20?')

for guessesTaken in range(5):
    guess = input('Take a guess: ')
    guess = int(guess)

    if guess < randomNumber:
        print ('Your guess is too low.')

    if guess > randomNumber:
        print ('Your guess is too high.')

    if guess == randomNumber:
        break

if guess == randomNumber:
    guessesTaken = str(guessesTaken + 1)
    print ('\nAmazing ' +name+ '! ' 'You guessed my number in ' \
           +guessesTaken+ ' guesses.')
    print ('\nPlay again!')

if guess != randomNumber:
    randomNumber = str(randomNumber)
    print ('\nSorry, but my number was ' +randomNumber+ '.')
    print ('\nDon\'t worry. Try again!')

input('\nThanks for playing! Press ENTER to exit and play again!.')
time.sleep(2)
exit()

