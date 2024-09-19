import time 
import json 
import os

class TodoList:
    def __init__(self,filepath='tasks.json') -> None:
        self.filepath = filepath
        self.tasks = []

    
    def save_tasks(self):
        with open(self.filepath,"w") as file:
            json.dump(self.tasks,file,indent=4)

