from datetime import timedelta
import datetime
class Task:

    taskName = ''
    duration = 0
    prerequisites = []
    startDate = datetime.datetime(2018,11,17)
    endDate = datetime.datetime(2018,11,17)
    maxDelay = 0
    


    def __init__(self, taskName = '', duration = 0, prerequisites = [], startDate = datetime.datetime(2018, 11, 17)):
        self.taskName = taskName
        self.duration = duration
        self.prerequisites = prerequisites
        self.startDate = startDate 
        # compute endDate
        if duration > 0:
            endDate = startDate + timedelta(days=duration)


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

    def getMaxDelay(self, maxDelay):
        return self.maxDelay 

    def toString(self):
        return ('taskName = ' + self.taskName + ';\nduration = ' + self.duration + ';\nprerequisites = ' + ','.join(self.prerequisites) + ';\nstartDate = ' + self.startDate + ';\nonCriticalPath = ' + str(self.onCriticalPath) + '\n\n')