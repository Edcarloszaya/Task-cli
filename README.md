# Task-cli 
simples solucao pra task-tracker do desafio de [roadmap.sh](https://roadmap.sh/backend/projects)

# como Iniciar
clone o repositorio e execute o seguinte comando:

git clone https://github.com/Edcarloszaya/Task-cli.git
cd Task-cli\task_cli\

## Como usar a ferramenta 

# Pra adiciona a task
python task-cli.py add "compra um livro"

# Pra atualizar a task  por id =1 ea descricao ="compra um livro e um marcado" 
python task-cli.py update 1 "compra um livro e um marcado"  

# Pra deletar a task por id = 1
python task-cli.py delete 1         

# Pra marca como completa por id = 1
python task-cli.py mark-done 1       

# Pra marca como pendecia por id igual a 1
python task-cli.py mark-in-progress 1   

# Pra lista todas as task
python task-cli.py list

# Pra lista todas as task por status done
python task-cli.py list_done

# Pra lista todas as task por status pendente
python task-cli.py list_in-progress

# ajudar detalhes dos comando 
python task-cli.py 