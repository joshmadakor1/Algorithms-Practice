'''
    Tandem Bicycle

    Write a function that takes in two arrays, representing the speeds
    of blue shirt and red shirt riders as well as an argument 'fastest'
    that will determine whether you calculate the slowest or fastest
    possible speeds. Each blue shirt rider will be paired with a red
    shirt rider. Return the slowest or fastest summed speed of all the
    riders depends on if fastest is set to true or false

    Time:  O(NlogN) + O(MlogM), where N and M = red/blue shirt riders
    Space: O(1)

    Last Practice: 2022-03-09 09:06:33
'''
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    sumOfSpeeds = 0
    redShirtSpeeds.sort()
    if fastest: blueShirtSpeeds.sort(reverse=True)
    else: blueShirtSpeeds.sort()
    for i in range(len(redShirtSpeeds)):
        sumOfSpeeds += max(redShirtSpeeds[i],blueShirtSpeeds[i])
    return sumOfSpeeds