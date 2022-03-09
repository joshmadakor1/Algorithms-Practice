'''
    CPU Scheduler:
    Given a CPU schedule with starting & ending time of
    processes. This schedule is used by the server to run
    the processes. When a new process comes into the scheduler,
    it is first checked with this scheduler if it can be
    accommodated or not.

    You have to return a boolean value if the incoming process
    can be accommodated into the process schedule or not. If it
    can be accommodated, then the scheduler has to be updated with
    the new process being a part of the schedule and if not then
    return false.

    Sample Input:
    currentSchedule = [["10:00","11:00"],["14:00","16:00"],["23:00","23:30"]]
    incomingProcesses = [["11:00","11:30"],["12:00","15:00"],["11:15","13:43"],["17:00","18:40"]]

    Sample Output:
    [True, False, False, True]

    Time: O(N*M), where N is the current schedule, and M is the incoming processes array
    Space: O(M), Where M is the result of the incoming process array

    Last Practiced: 2022-03-09 12:47:00
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
