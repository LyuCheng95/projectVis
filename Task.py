import datetime
class Task:

    taskName = ''
    duration = 0
    prerequisites = []
    startDate = datetime.datetime(2018,11,17)
    setOnCriticalPath = False


    def setTaskName(self, taskName):
        self.taskName = taskName

    def setDuration(self, duration):
        self.duration = duration
        
    def setPrerequisites(self, prerequisites):
        self.prerequisites = prerequisites

    def setStartDate(self, startDate):
        self.startDate = startDate 

    def setOnCriticalPath(self, onCriticalPath):
        self.onCriticalPath = onCriticalPath 