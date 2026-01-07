from datetime import datetime
import json

class Tarefa:
    def __init__(self, titulo, descricao, prazo=None):
        self._titulo=titulo
        self._descricao=descricao
        self._prazo=prazo
        self.concluida=False
        self.criacao=datetime.now()
    
    def concluir(self):
        self.concluida=True
    
    def __str__(self):
        status='Concluida' if self.concluida else 'Pendente'
        prazo=f'Prazo: {self._prazo}' if self._prazo else 'Sem prazo definido'
        return (
            f'Titulo: {self._titulo}\nDescrição: {self._descricao}\nStatus: {status}\n{prazo}\n'
        )
    
    #converter para dicionario - salvar em json depois
    def to_dict(self):
        return{
            "titulo":self._titulo,
            "descricao":self._descricao,
            "prazo":self._prazo,
            "concluida":self.concluida
        }
       
    #criar tarefa a partir de dicionario
    @staticmethod
    def from_dict(dados):
        return Tarefa(dados["titulo"],dados["descricao"],dados["prazo"],dados["concluida"])
        
    
