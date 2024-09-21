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
        "createdAt":datetime.now().strftime("%Y-%m-%d %H:%M"),
        "updatedAt":"",
        }
        self.tasks.append(task)
        self.save_tasks()
        print('\nTask added\n')

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
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.save_tasks()
            print(f'\ntask updated\n')
           
        else:
            print(f"\nTask with ID {id} not found.\n")
          
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
            print('\ntask deleted\n')

        else:
            print('\nTask with {id} not found\n')
        
    def mark_in_progress(self,id):
        """"atualiza o status da task pra in progress"""
        task = self.get_task_by_id(id)
        if task:
            task["status"] = "in-progress"
            self.save_tasks()
            print(f"\nTask {id} marked in-progress\n")

        else:
            print(F'\nTask {id} not found\n')

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
            task["status"] = "done"
            self.save_tasks()
            print(f"\nTask {id} marked done\n")

        else:
            print(F'\nTask {id} not found\n')
        
    def list(self):
        for task in self.tasks:
            
            print(f"\nid:{task['id']} description:{task['description']} status:{task['status']} created:{task['createdAt']} updated:{task['updatedAt']}")

        print(" ")
            
    def list_done(self,done):
        self.get_task_status(done)

    def list_in_progress(self,in_progress):
        self.get_task_status(in_progress)

    def get_task_status(self,status):
        """ retorna uma task pelo id"""
        for task in self.tasks:
            if task["status"] == status:
                print(f"\nid:{task['id']} description:{task['description']} status:{task['status']} created:{task['createdAt']} updated:{task['updatedAt']}")
        
        print(" ")
            
        return None

