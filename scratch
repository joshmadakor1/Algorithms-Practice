import datetime

def checkWhichJobsCanBeScheduled(currentSchedule, incomingProcesses):
    result = []
    convertSchedulesToDatetime(currentSchedule)
    convertSchedulesToDatetime(incomingProcesses)


def convertSchedulesToDatetime(schedules):
    for index, element in enumerate(schedules):
        startHour, startMinute = element[0].split(":")
        endHour, endMinute = element[1].split(":")
        schedules[index][0] = datetime.datetime.now().replace(hour=int(startHour), minute=int(startMinute), second=0, microsecond=0)
        schedules[index][1] = datetime.datetime.now().replace(hour=int(endHour), minute=int(endMinute), second=0, microsecond=0)
        print(schedules[index])
        


currentSchedule = [["10:00","11:00"],["14:00","16:00"],["23:00","23:30"]]
incomingProcesses = [["11:00","11:30"],["12:00","15:00"],["11:15","13:43"],["17:00","18:40"]]


checkWhichJobsCanBeScheduled(currentSchedule, incomingProcesses)