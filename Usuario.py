import json

class Usuario:
    def __init__(self,nome):
        self._nome=nome
        self._tarefas=[]
        
    def adicionar_tarefa(self,tarefa):
        self._tarefas.append(tarefa)
    
    def listar_tarefas(self):
        for i, tarefa in enumerate(self._tarefas,1):
            print(f'{i} - {tarefa}')
            
    #salvar tarefas em um arquivo json
    def salvar_tarefas(self):
        with open(f"{self._nome}_tarefas.json","w",encoding="utf-8") as file:
            json.dump([t.to_dict() for t in self._tarefas], file, ensure_ascii=False,indent=4)
            print('Arquivo JSON salvo com sucesso')
    
    #ler dados no arquivo json
    def carregar_tarefas(self):
        try:
            with open(f"{self._nome}_tarefas.json","r",encoding="utf-8") as file:
                dados=json.load(file)
                self._tarefas=[Tarefa.from_dict(d) for d in dados]
        except FileNotFoundError:
            self._tarefas=[]
            print('Arquivo não encontrado')
