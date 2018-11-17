import datetime
class Transition:
    parentTask = Task()
    childTask = Task()
    delay = 0

    def setParentTask(self, parentTask):
        self.parentTask = parentTask


    def setChildTask(self, childTask):
        self.childTask = childTask

    def setDelay(self, delay):
        self.delay = delay 