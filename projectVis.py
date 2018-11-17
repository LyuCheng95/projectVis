import csv
import datetime
import Task 
import Transition
import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict
from collections import deque

inputFileName = 'InputData.csv'


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

def getSortedEndTasks(project):
    leafTasks = {} 

    # find all leaf nodes
    for item in project.out_degree:
        if item[1] == 0:
            leafTasks[item[0]] = None 

    # assign end date 
    for nodeName in leafTasks:
        endDate = project.nodes[nodeName]['task'].getEndDate()
        leafTasks[nodeName] = endDate

    # sort the task according to timestamp
    sortedTasks = OrderedDict(sorted(leafTasks.items()))
    endTasks = list(sortedTasks.keys())
    return endTasks 

def getProjectEndDate(project, endTasks):
    return project.nodes[endTasks[0]]['task'].getEndDate()

def computeMaxDelay(project):
    tasks = deque(getSortedEndTasks(project))
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
                maxDelay = 0
                for successor in succList:
                    successorTask = project.nodes[successor]['task']
                    succStartDate = successorTask.getStartDate()
                    endDate = task.getEndDate()
                    gap = (succStartDate - endDate).days
                    possibleDelay = gap + successorTask.getMaxDelay()
                    if possibleDelay > maxDelay:
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
            # maxDelay = 
            # currTask.set

def computePrepareTime(project):
    for taskName in project:
        project.nodes[taskName]['task'].computePrepareTime()

def getCriticalPath(project):
    criticalPath = []
    for taskName in project:
        if project.nodes[taskName]['task'].getMaxDelay() == 0:
            criticalPath.append(taskName)
    return criticalPath

project = prepareProjectGraph(inputFileName)
computeMaxDelay(project)
computePrepareTime(project)
criticalPath = getCriticalPath(project)
for task in project.nodes:
    project.nodes[task]['task'].printDetails()
print(criticalPath)
