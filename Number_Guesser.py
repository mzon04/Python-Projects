import sys
from random import randint

TargetValue=randint(1,100)
while 1:
    Guess=int(input("Enter guess between 1 and 100: "))
    if Guess == TargetValue:
        print ("Correct")
        break

    if Guess > TargetValue :
        print ("Lower\n")
    elif Guess < TargetValue:
        print ("Higher\n")