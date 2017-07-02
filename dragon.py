#Topics Covered In This Chapter:
#·        The time.sleep() function
#·        Creating your own functions with the def keyword
#·        The return keyword
#·        The and, or, and not Boolean operators
#·        Truth tables
#·        Global and local variable scope
#·        Parameters and Arguments
#·        Flow charts

import random
import time

def displayIntro():
    print ('----------------------')
    print ('     Dragon Realm')
    print ('----------------------')
    print ('You are in a land full of dragons. In front of you,')
    print ('you see two caves. In one cave, the dragon is friendly')
    print ('and will share his treasure with you. The other dragon')
    print ('is greedy and hungry, and will eat you on sight.')
    print ()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print ('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave


def friendlyCave():
    print('Gives you his treasure!')
    time.sleep(1)


def creepyCave():
    print('Gobbles you down in one bite!')
    time.sleep(1)


def checkCave(chosenCave):
    print ('You approach the cave...')
    time.sleep(1)
    print ('It is dark and spooky...')
    time.sleep(1)
    print ('A large dragon jumps out in front of you! He opens his jaws and...')
    time.sleep(1)

    if chosenCave == random.randint(1,2):
        friendlyCave()
    else:
        creepyCave()


displayIntro()
playing = 'yes'

while playing == 'yes' or playing == 'y':
    chosenCave = chooseCave()
    chosenCave = int(chosenCave)
    checkCave(chosenCave)

    print('Do you want to play again? (yes or no)')
    playing = input()
