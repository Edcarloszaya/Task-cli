import argparse

parser = argparse.ArgumentParser(description="To-Do List CLI App")

# Subcomandos
subparsers = parser.add_subparsers(dest="command")

# Comando para adicionar uma tarefa
add = subparsers.add_parser("add", help="add task to the Todo-list")
add.add_argument("description", type=str, help="descrition from the task ")

# Comando para atualiza as tarefas
update = subparsers.add_parser("update", help="update task to the Todo-list")
update.add_argument("id", type=int, help="id of the task that will be updated ")
update.add_argument("description", type=str, help="descrition from the task ")

# Comando para deleta uma tarefa
delete = subparsers.add_parser("delete", help="delete a task from id")
delete.add_argument("id", type=int, help="id of the task that will be deleted")

# Comando para completar uma tarefa
mark_done = subparsers.add_parser("mark-in-done", help="mark done task from id")
mark_done.add_argument("id", type=int, help="id of the task that will be marked done")

# Comando para marca que pendente a task
marke_in_progress = subparsers.add_parser(
    "mark-in-progress", help="mark in-progress task from id"
)
marke_in_progress.add_argument(
    "id", type=int, help="id of the task that will be marked in-progress"
)

# Comando para listar todas as tarefas
list_all = subparsers.add_parser("list", help="list all stored tasks")

# Comando para listar todas as tarefas com satus completo
list_done = subparsers.add_parser(
    "list_done", help="list all stored tasks marked done"
)


# Comando para listar todas as tarefas com satus pendente
list_in_progress = subparsers.add_parser(
    "list_in-progress", help="list all stored tasks marked in-progress"
)


# Parse dos argumentos
args = parser.parse_args()

