def nthFib(n):
    memo = {}
    return nthFibHelper(n, memo)

def nthFibHelper(n, memo):
    if n <= 2:
        if n not in memo:
            memo[n] = 1
            return memo[n]
    else:
        if (n-1) not in memo:
            memo[n-1] = nthFibHelper(n-1, memo)
        if (n-2) not in memo:
            memo[n-2] = nthFibHelper(n-2, memo)
        return memo[n-1] + memo[n-2]


print(nthFib(100))