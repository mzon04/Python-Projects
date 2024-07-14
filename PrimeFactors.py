import array

def main():
    InputPrompt=input("Enter a positive integer: ")
    try :
        num = int(InputPrompt)
    except ValueError :
        print(f"\"{InputPrompt}\" is not a number")
        exit()

    if num < 0:
        print(f"\"{InputPrompt}\" is a negative number")
        exit()

    if num == get_factor(num) :
        print(f"\"{num}\" is Prime")
        exit()



    Factors = [num]
    while True:
        LastFactor = Factors.pop()
        NewFactor = get_factor(LastFactor)
        if LastFactor == NewFactor:
            Factors.insert(len(Factors),LastFactor)
            break
        Factors.insert(len(Factors),NewFactor)
        Factors.insert(len(Factors),int(LastFactor/NewFactor))
    
    print(f"Final Factors: {Factors}")
        

def get_factor(num):
    TestFactor=2
    while TestFactor <= num/2:
        remainder = num % TestFactor
        if remainder == 0:
            return TestFactor
        TestFactor += 1
    
    return num



#define function to find factor for number
main()