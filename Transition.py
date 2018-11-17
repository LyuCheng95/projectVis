import datetime
import Task
class Transition:
    parentTask = Task.Task()
    childTask = Task.Task()
    delay = 0

    def __init__(self, parentTask = Task.Task(), childTask = Task.Task(), delay = 0):
        self.parentTask = parentTask 
        self.childTask = childTask 
        self.delay = delay

    def setParentTask(self, parentTask):
        self.parentTask = parentTask

    def setChildTask(self, childTask):
        self.childTask = childTask

    def setDelay(self, delay):
        self.delay = delay