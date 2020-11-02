def aCalc(userA):
    if "x" in userA:
        operatorIndex = userA.index("x")
        num1 = userA[0:operatorIndex]
        num2 = userA[(operatorIndex+1):]
        product = int(num1) * int(num2)
        return product
    elif "/" in userA:
        operatorIndex2 = userA.index("/")
        num1b = userA[0:operatorIndex2]
        num2b = userA[(operatorIndex2+1):]
        quotient = int(num1b) / int(num2b)
        return quotient
    elif "+" in userA:
        operatorIndex3 = userA.index("+")
        num1c = userA[0:operatorIndex3]
        num2c = userA[(operatorIndex3+1):]
        total = int(num1c) + int(num2c)
        return total
    elif "-" in userA:
        operatorIndex4 = userA.index("-")
        num1d = userA[0:operatorIndex4]
        num2d = userA[(operatorIndex4+1):]
        difference = int(num1d) + int(num2d)
        return difference

def calcLog(userA, ansUserA):
    logA = userA + " = " + str(ansUserA)
    return logA
    
def main():
    newList = []
    mathProb = input("Enter calculation: ")
    while True:
        ansUserA= aCalc(mathProb)
        logA = calcLog(mathProb, ansUserA)
        newList.append(logA)
        if len(newList) <= 10:
            for elm in newList:
                print(elm)
        elif len(newList) >10:
            subList = newList[-10:]
            for elm in subList:
                print(elm)
        mathProb = input("Enter calculation: ")
                     

main()
