import array

def main():
    InputPrompt=input("Input starting number: ")
    try :
        num = int(InputPrompt)
    except ValueError :
        print(f"\"{InputPrompt}\" is not a number")
        exit()

    if num < 0:
        print(f"\"{InputPrompt}\" is a negative number")
        exit()

    InputPrompt = "Y"
    while InputPrompt == "Y" or "y":
        num +=1
        while num != get_factor(num):
            num += 1

        print(f"\"{num}\" is the next Prime")
        InputPrompt = input("Continue [Y/N]? ")

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