import sys
import os

Answer=input("Input Answer: ")
Blank={}
os.system("cls")
print ("Answer is recorder")
index=0
for x in Answer:
    Blank[index]="*"
    index=index+1

def get_hidden(Blank):
    Hidden=""
    for x in Blank:
        Hidden=Hidden+Blank[x]
    return Hidden

while 1:
    print ("Hidden answer :",get_hidden(Blank))
    Guess=input("Guess: ")
    if len(Guess) == 1:
        counter=0
        index=0
        for x in Answer:
            if Guess == x:
                Blank[index]=x
                counter=counter+1
            index=index+1
        os.system("cls")
        print (counter,Guess,"found.")
        if get_hidden(Blank) == Answer:
            print ("Answer:",get_hidden(Blank))
            print ("Your guess is correct. Eyyyyyy!!!!")
            break
        
    
    if len(Guess) > 1:
        if Guess == Answer:
            os.system("cls")
            print ("Answer:",Guess)
            print ("Your guess is correct. Eyyyyyy!!!!")
            break
        else:
            os.system("cls")
            print ("Your guess is incorrect")



        