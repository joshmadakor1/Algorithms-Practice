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
import datetime

def jobsThatCanBeScheduled(currentSchedule, incomingProcesses):
    result = []
    convertSchedulesToDatetime(currentSchedule)
    convertSchedulesToDatetime(incomingProcesses)
    for process in incomingProcesses:
        checkForOverlap(process, currentSchedule, result)
    return result

def checkForOverlap(process, currentSchedule, result):
    for currentJob in currentSchedule:
        if (not (process[0] > currentJob[0] and process[0] < currentJob[1])) and (not (process[1] > currentJob[0] and process[1] < currentJob[1])):
            continue
        else:
            result.append(False)
            return
    # If the current process fits the schedule, append it to the currentSchedule tasks
    result.append(True)
    currentSchedule.append(process)

def convertSchedulesToDatetime(schedules):
    for index, element in enumerate(schedules):
        startHour, startMinute = element[0].split(":")
        endHour, endMinute = element[1].split(":")
        schedules[index][0] = datetime.datetime.now().replace(hour=int(startHour), minute=int(startMinute), second=0, microsecond=0)
        schedules[index][1] = datetime.datetime.now().replace(hour=int(endHour), minute=int(endMinute), second=0, microsecond=0)        


currentSchedule = [["10:00","11:00"],["14:00","16:00"],["23:00","23:30"]]
incomingProcesses = [["11:00","11:30"],["12:00","15:00"],["11:15","13:43"],["17:00","18:40"]]


print(jobsThatCanBeScheduled(currentSchedule, incomingProcesses))
