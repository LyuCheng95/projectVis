import csv
import datetime
import Task 
import Transition
import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict
from collections import deque

inputFileName = './InputData.csv'


def prepareProjectGraph(fileName):
    # initialize project graph
    project = nx.DiGraph()
    # read file
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # add task as node in project
            dateList = row['start_date'].split('/')
            day = int(dateList[0])
            month = int(dateList[1])
            year = int(dateList[2])
            startDate = datetime.datetime(year, month, day)
            task = Task.Task(row['task_name'], int(row['duration']), row['prerequisites'].split(';'), startDate)
            project.add_node(row['task_name'], task = task)

    # create Transition objects as edges
    for taskName in project.nodes:
        currentTask = project.nodes[taskName]['task']
        prerequisitesList = currentTask.getPrerequisites()
        for prerequisite in prerequisitesList:
            if prerequisite != '':
                parentTask = project.nodes[prerequisite]['task']
                transition = Transition.Transition(parentTask, currentTask, 0)
                project.add_edge(prerequisite, taskName, transition = transition)
    return project

def getEndTasks(project):
    endTasks = [] 

    # find all leaf nodes
    for item in project.out_degree:
        if item[1] == 0:
            endTasks.append(item[0]) 
    return endTasks

def getProjectEndDate(project, endTasks):
    # dictonary task name : end date
    sortedTasks = {}
    for taskName in endTasks:
        sortedTasks[taskName] = project.nodes[taskName]['task'].getEndDate()
    sortedTasks = OrderedDict(sorted(sortedTasks.items(), key=lambda x: x[1]))
    return sortedTasks[list(sortedTasks.keys())[-1]] 

def computeMaxDelay(project):
    tasks = deque(getEndTasks(project))
    projectEndDate = getProjectEndDate(project, tasks)
    # dealing with each task, starting from end
    seen = set(tasks)
    while True: 
        # exit when task list is empty
        if not tasks:
            break
        else:
            taskName = tasks.popleft()
            task = project.nodes[taskName]['task']
            succList = list(project.successors(taskName))
            if succList:
                # possibleDelay = gap + successor's maxDelay
                # compare among possibleDelay from successors
                maxDelay = 10000
                for successor in succList:
                    successorTask = project.nodes[successor]['task']
                    succStartDate = successorTask.getStartDate()
                    endDate = task.getEndDate()
                    gap = (succStartDate - endDate).days
                    possibleDelay = gap + successorTask.getMaxDelay()
                    if possibleDelay < maxDelay:
                        maxDelay = possibleDelay
                task.setMaxDelay(maxDelay)
            else:
                # if there is no successor, compare with the project end date
                deltaDate = projectEndDate - task.getEndDate()
                maxDelay = deltaDate.days
                task.setMaxDelay(maxDelay)
            # push in prerequisites if there are some
            for prerequisite in task.getPrerequisites():
                if prerequisite not in seen and prerequisite != '':
                    seen.add(prerequisite)
                    tasks.append(prerequisite) 

def computeArrivalTime(project):
    for taskName in project:
        task = project.nodes[taskName]['task']
        task.computePrepareTime()
        task.computeArrivalTime()

def getCriticalPath(project):
    criticalPath = []
    for taskName in project:
        if project.nodes[taskName]['task'].getMaxDelay() == 0:
            criticalPath.append(taskName)
    return criticalPath

project = prepareProjectGraph(inputFileName)
computeMaxDelay(project)
computeArrivalTime(project)
criticalPath = getCriticalPath(project)
for task in project.nodes:
    project.nodes[task]['task'].printDetails()
print(criticalPath)
