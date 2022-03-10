def getNthFib(n):
    dict = {}
    return memoizationHelper(n, dict, 0)
    

def memoizationHelper(n, dict, numberOfCalls):
    
    print(numberOfCalls)
    if n <= 2:
        if n in dict: return dict[n]
        dict[n] = 1
        return dict[n]
    else:
        if not (n-1) in dict:
            numberOfCalls += 1
            dict[n-1] = memoizationHelper(n-1, dict, numberOfCalls)
        if not (n-2) in dict:
            numberOfCalls += 1
            dict[n-2] = memoizationHelper(n-2, dict, numberOfCalls)
        return dict[n-1] + dict[n-2]

def slowFib(n, numberOfCalls):
    print(numberOfCalls)
    if n <= 2:
        return 1
    else:
        numberOfCalls[0] += 1
        a = slowFib(n-1,numberOfCalls)
        numberOfCalls[0] += 1
        b = slowFib(n-2,numberOfCalls)
        return a+b 

print(getNthFib(30))
#print(slowFib(30,[0]))