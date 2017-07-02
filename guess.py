## This is a guess the Number game
#import for choosing random number
import random

#initiate guessing Num
gNum = 0

#Asking a player name
print ('Hello! What is your name?')
pName = input()

#pick a random number
print ('Well, ' + pName + '. I am thinking of a number between 1 and 20.')
number = random.randint(1,20)

numGuessed = 0
while numGuessed < 6:
    print ('Take a guess.')
    gNum = input()
    gNum = int(gNum)
    numGuessed = numGuessed + 1

    if number > gNum:
      print ('Your guess is too low.')

    if number < gNum:
      print ('Your guess is too high.')

    if number == gNum:
        numGuessed = str(numGuessed)
        print ('Good job, ' + pName + '! You guessed my number in ' + numGuessed + ' guesses!')
        break

if number != gNum:
    number = str(number)
    print ('Sorry. The number I was thinking of was ' + number)
