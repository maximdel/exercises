from datetime import *

class Task:
    def __init__(self, description, due_date):
        self.__description = description
        self.__due_date = due_date
        self.__finished = False
        
    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def description(self):
        return self.__description

    

class TaskList:
    def __init__(self):
        self.__list = []
        
    def __len__(self):
        return len(self.__list)

    def add_task(self, task):
        if task.due_date < date.today():
            raise RuntimeError("Date incorrect")
        self.__list.append(task)

    @property
    def finished_tasks(self):
        return list(task for task in self.__list if task.finished)
    
    @property
    def due_tasks(self):
        return list(task for task in self.__list if not task.finished)

    @property
    def overdue_tasks(self):
        return list(task for task in self.__list if not task.finished and task.__due_date < date.today())