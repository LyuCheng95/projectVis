import csv
import datetime
import Task 
import Transition
import networkx as nx
import matplotlib.pyplot as plt

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
                transitionName = parentTask.getTaskName() + '_to_' + taskName 
                transition = Transition.Transition(parentTask, currentTask, 0)
                project.add_edge(prerequisite, taskName, transition = transition)
    return project

def getLeafTasks(project):

    return []



project = prepareProjectGraph(inputFileName)
print(project.nodes)
leafTasks = getLeafTasks(project)

