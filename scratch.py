
# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum' 
# otherwise returns
# false. Also, prints
# the result 


def subArraySum(arr, n, sum_):
    count = 0
    # Pick a starting 
    # point
    for i in range(n):
        curr_sum = arr[i]
    
        # try all subarrays
        # starting with 'i'
        j = i + 1
        while j <= n:
            count +=1
            print("count,", count)
            if curr_sum == sum_:
                print ("Sum found between")
                print("indexes % d and % d"%( i, j-1))
                
                return 1
                
            if curr_sum > sum_ or j == n:
                break
            
            curr_sum = curr_sum + arr[j]
            j += 1

    print ("No subarray found")
    return 0

# Driver program 
arr = [2, 4, 8, 5, 9, 10, 15, 99]
n = len(arr)
sum_ = 23

subArraySum(arr, n, sum_)

# This code is Contributed by shreyanshi_arun.