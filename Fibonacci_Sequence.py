print("Generate nth number in Fibonnaci sequence")
InputStr = input("What is n? ")
try:
    n = int(InputStr)
except ValueError:
    print(f"\"{InputStr}\" is not an integer")
    exit()

seq = {}
seq[0] = 0
seq[1] = 1
if n < 0:
    print(f"\"{InputStr}\" is negative. Please input positive integer")
    exit()

if n > 1:
    for i in range(n):
        seq[i+2] = seq[i+1] + seq[i]


nLast = InputStr[len(InputStr)-1]

match nLast:
    case "1":
        OrderSuffix = "st"
    case "2":
        OrderSuffix = "nd"
    case "3":
        OrderSuffix = "rd"
    case _:
        OrderSuffix = "th"


print(f"{n}{OrderSuffix} number is {seq[n]}")