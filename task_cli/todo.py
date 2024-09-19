from datetime import datetime
import json 
import os

class TodoList:
    def __init__(self,filepath='tasks.json') -> None:
        self.filepath = filepath
        self.tasks = self.load_tasks()

    
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
        print('Task added')

    def create_id(self):
        ''' cria um id unico'''

        if not self.tasks:
            return 1
        else:
            max_1 = max(task["id"] for task in self.tasks)
            return max_1 + 1

    def update(self,id,new_description):
        ''' edita a task com base no id'''

        task = self.get_task_by_id(id)
        if task:
            task["description"] = new_description
            task["updateAt"] = datetime.now().isoformat()
            self.save_tasks()
            print(f'task updated')
           
        else:
            print(f"Task with ID {id} not found.")
          
    def load_tasks(self):
        """Carrega as tarefas de um arquivo JSON ou cria o arquivo se não existir."""
        if not os.path.exists(self.filepath):
            # Se o arquivo não existir, cria um arquivo JSON vazio
            with open(self.filepath, 'w') as file:
                json.dump([], file)
            return []
        else:
            with open(self.filepath, 'r') as file:
                return json.load(file)

    def delete(self,id):
        '''deleta a tesk pelo id'''
        task = self.get_task_by_id(id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print('task deleted')

        else:
            print('Task with {id} not found')
        
    def mark_in_progress(self,id):
        """"atualiza o status da task pra in progress"""
        task = self.get_task_by_id(id)
        if task:
            task["status"] = "marked-in-progress"
            self.save_tasks()
            print(f"Task {id} marked in-progress")

        else:
            print(F'Task {id} not found')

    def get_task_by_id(self,id):
        """ retorna uma task pelo id"""
        for task in self.tasks:
            if task["id"] == id:
                return task
            
        return None
    
    def mark_done(self,id):
        """"atualiza o status da task pra done"""
        task = self.get_task_by_id(id)
        if task:
            task["status"] = "marked-done"
            self.save_tasks()
            print(f"Task {id} marked done")

        else:
            print(F'Task {id} not found')
        
    


td = TodoList()
td.mark_done(1)