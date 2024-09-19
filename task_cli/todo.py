from datetime import datetime
import json 
import os

class TodoList:
    def __init__(self,filepath='tasks.json') -> None:
        self.filepath = filepath
        self.tasks = []

    
    def save_tasks(self):
        ''' salva a task'''

        with open(self.filepath,"w") as file:
            json.dump(self.tasks,file,indent=4)

    def add(self,description):
        ''' cria uma task'''

        task = {
        "id":self.create_id(),
        "description":f'{description}',
        "status":"in-progress",
        "createdAt":datetime.now().isoformat(),
        "updateAt":"",
        }
        self.tasks.append(task)
        self.save_tasks()

    def create_id(self):
        ''' cria um id unico'''

        if not self.tasks:
            return 1
        else:
            max_1 = max(task["id"] for task in self.tasks)
            return max_1 + 1
        
# td = TodoList()
# td.add("test")