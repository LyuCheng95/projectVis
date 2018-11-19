from datetime import timedelta
import datetime
class Task:

    taskName = ''
    duration = 0
    prerequisites = []
    startDate = datetime.datetime(2018,1,1)
    endDate = datetime.datetime(2018,1,1)
    maxDelay = 0
    prepareTime = 0
    arrivalTime = datetime.datetime(2018,1,1)

    def __init__(self, taskName = '', duration = 0, prerequisites = [], startDate = datetime.datetime(2018, 1, 1)):
        self.taskName = taskName
        self.duration = int(duration)
        self.prerequisites = prerequisites 
        self.startDate = startDate 
        # compute endDate
        if duration > 0:
            self.endDate = startDate + timedelta(days=duration)
        else:
            self.endDate = startDate

    def setTaskName(self, taskName):
        self.taskName = taskName

    def setDuration(self, duration):
        self.duration = duration
        
    def setPrerequisites(self, prerequisites):
        self.prerequisites = prerequisites

    def setStartDate(self, startDate):
        self.startDate = startDate 

    def setMaxDelay(self, maxDelay):
        self.maxDelay = maxDelay 

    def getTaskName(self):
        return self.taskName 

    def getDuration(self):
        return self.duration

    def getPrerequisites(self):
        return self.prerequisites

    def getStartDate(self):
        return self.startDate

    def getOnCriticalPath(self):
        return self.onCriticalPath

    def getMaxDelay(self):
        return self.maxDelay 

    def getEndDate(self):
        return self.endDate 

    def computePrepareTime(self):
        if self.maxDelay == 0:
            self.prepareTime = 2 
        else:
            self.prepareTime = 1

    def computeArrivalTime(self):
        self.arrivalTime = self.startDate - timedelta(days = self.prepareTime)

    def printDetails(self):
        return print(
            'taskName = ', self.taskName, 
            '\nduration = ', self.duration, 
            '\nprerequisites = ', ','.join(self.prerequisites), 
            '\nstartDate = ', self.startDate, 
            '\nendDate = ', self.endDate, 
            '\nmaxDelay = ', str(self.maxDelay), 
            '\nprepareTime = ', self.prepareTime,
            '\narrivalTime = ', self.arrivalTime,
            '\n'
        )