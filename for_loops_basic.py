
for i in range (1,151,1):
    print(i)


for num in range (5,1005,1):
    if num % 5 == 0:
        print(num)

def countingTheDojoWay():
    for num in range(1,100,1):
        if num % 10 == 0:
            print("Coding Dojo")
        elif num % 5 == 0:
            print("Coding")
        else: print(num)
print(countingTheDojoWay())

def whoaThatSuckersHuge():
    sum = 0
    for num in range(500000):
        if num % 2 == 1:
            sum+=num
            print(num)
    print(sum)
whoaThatSuckersHuge()

def countingByFours():
    for num in range (2018, 1 , -4):
        print(num)
countingByFours()

def flexibleCounters():
    lowNum = 2
    highNum = 9
    mult = 3
    for num in range (lowNum,highNum+1):
        if num % mult == 0:
            print(num)