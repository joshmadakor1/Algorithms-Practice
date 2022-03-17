'''
    Nth Fibonacci:

    Write a function that takes an in integer greater 0 and prints out the
    Nth fibonacci sequence

    Time:  O(N), where N is the value of the input integer
    Space: O(D) -> O(N) where N is the size of the recursive callstack

    LastPracticed: 2022-03-17 08:31:39
'''
def getNthFib(n):
    array = [None] * (n+1)
    nthFibDynamic(n, array)
    return array[n]

def nthFibDynamic(n, array):
    if n == 1:
        array[1] = 0
        return array[1]
    elif n == 2:
        array[2] = 1
        return array[2]
    else:
        if array[n] is None:
            array[n] = nthFibDynamic(n-1, array) + nthFibDynamic(n-2, array)
        return array[n]
    
