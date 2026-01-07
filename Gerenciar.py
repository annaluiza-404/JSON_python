class Gerenciar:
    def __init__(self):
        self._usuarios={}
        
    def adicionar_usuarios(self,usuario):
        self._usuarios[usuario.nome]=usuario
        
    def listar_usuarios(self):
        for nome in self._usuarios:
            print(f'- {nome}')
    
    
