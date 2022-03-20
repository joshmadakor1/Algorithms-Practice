def search(array, target):
    return helper(array, target, 0, len(array))

def helper(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    
    if array[mid] == target:
        return mid

    if target < array[mid] and target >= array[left]:
        return helper(array, target, left, mid -1)
    else:
        return helper(array, target, mid + 1, right)
    

print(search([4,5,6,7,0,1,2],0))